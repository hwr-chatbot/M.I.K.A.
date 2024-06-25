from rasa.core.policies import FallbackPolicy
from rasa.engine.recipes import DefaultV1Recipe

@DefaultV1Recipe.register("FallbackPolicy")
class MyFallbackPolicy(FallbackPolicy):
    def __init__(self, nlu_threshold: float = 0.3, core_threshold: float = 0.3):
        super().__init__(nlu_threshold, core_threshold)
