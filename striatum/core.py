from striatum import make_logger
from pandas import DataFrame
import dask.bag as db
from dask import get
import matplotlib.pyplot as plt

logger = make_logger(__file__)


class TestBed:
    df_meta = {'action': int,
               'reward': float,
               'step': int,
               'best-action': int,
               'episode': int}

    def __init__(self, dsk, analyses, scheduler='processes'):
        self.name_ = dsk.get('name') if 'name' in dsk.keys() else 'no-name'
        self.scheduler = scheduler
        self.data = DataFrame()
        self.analyses = analyses
        self.dsk = dsk

    def run(self, n_steps, n_episodes=1):
        self.n_steps = n_steps
        self.n_episodes = n_episodes
        params_vec = [self.sample_dsk(d) for d in n_episodes*[self.dsk]]
        if n_episodes > 1:
            self.data = (db.from_sequence([(n_steps, episode,
                                            params_vec[episode])
                                           for episode in range(n_episodes)])
                           .starmap(self.single_run)
                           .flatten()
                           .to_dataframe()
                           .compute(scheduler=self.scheduler)
                           .reset_index())
        else:
            self.data = DataFrame(self.single_run(n_steps, 0, params_vec[0]))
        return self

    def single_run(self, n_steps, episode, params):
        perc = round(100*episode/self.n_episodes, 2)
        logger.info(f'episode={episode}/{self.n_episodes} ({perc}%)')
        policy, env, policy_params, env_params = self._apply_params(params)
        data = list()
        for step in range(n_steps):
            action = policy.sample()
            best_action = env.avf.best_action
            reward = env.step(action)
            policy.update_from_step(reward)
            data += [self.format_data(step, action, best_action, reward,
                                      episode, policy_params, env_params)]
        return data

    def plot(self):
        for a in self.analyses:
            logger.info(f'Plotting {a.name}')
            a.episode(self.data).plot()

    def save(self):
        dir_path = f'results/{self.name_}'
        logger.info(f'Saving data for {dir_path}')
        self.data.to_pickle(f'{dir_path}/data.pkl')
        for a in self.analyses:
            plt.figure()
            logger.info(f'Saving {a.name}')
            a.episode(self.data).save_to(dir_path)

    def sample_dsk(self, dsk):
        return dict(zip(dsk, get(dsk, list(dsk.keys()))))
