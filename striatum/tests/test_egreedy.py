from striatum import policies
from gym import spaces


class Test_EpsilonGreedy:
    def setup(self) -> None:
        class TestEnv:
            action_space = spaces.Discrete(3)

        epsilon = 0.2
        def decay(N): return 0.9/N
        self.policy = policies.EpsilonGreedy(env=TestEnv(),
                                             epsilon=epsilon,
                                             decay=decay)

    def update(self):
        # first step
        self.policy.latest_action = 0
        self.policy.update(1.0)

        assert self.policy.n_action_sampled[0] == 1
        assert self.policy.n_action_sampled[1] == 0
        assert self.policy.n_action_sampled[2] == 0

        assert self.policy.avf_estimate[0] == 1.0
        assert self.policy.avf_estimate[1] == 0.0
        assert self.policy.avf_estimate[2] == 0.0

        # second step
        self.policy.latest_action = 1
        self.policy.update(2.0)

        assert self.policy.n_action_sampled[0] == 1
        assert self.policy.n_action_sampled[1] == 1
        assert self.policy.n_action_sampled[2] == 0

        assert self.policy.avf_estimate[0] == 1.0
        assert self.policy.avf_estimate[1] == 2.0
        assert self.policy.avf_estimate[2] == 0.0

        # third step
        self.policy.latest_action = 1
        self.policy.update(0.0)

        assert self.policy.n_action_sampled[0] == 1
        assert self.policy.n_action_sampled[1] == 2
        assert self.policy.n_action_sampled[2] == 0

        assert self.policy.avf_estimate[0] == 1.0
        assert self.policy.avf_estimate[1] == 1.0
        assert self.policy.avf_estimate[2] == 0.0

    def test_sample_greedy(self) -> None:
        self.policy.latest_action = 2
        self.policy.update(10)
        self.policy.sample_greedy() == 2
