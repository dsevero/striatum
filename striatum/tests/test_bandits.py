from striatum import envs, utils


class Test_MultiArmedBandit:
    def setup(self) -> None:
        n_arms = 3
        self.average_rewards = [0, 1, 2]
        reward_noise_rv = utils.constant(0)
        self.env = envs.MultiArmedBandit(n_arms=n_arms,
                                         average_rewards=self.average_rewards,
                                         reward_noise_rv=reward_noise_rv)

    def test_step(self) -> None:
        assert all(self.env.step(i) == (None, i, False, {})
                   for i in self.average_rewards)
