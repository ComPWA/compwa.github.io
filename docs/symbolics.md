# Symbolic amplitude models

Amplitude analysis attempts to describe the intensity distributions that we observe in particle collider experiments in order to extract parameters about intermediate states appearing in the scattering process. The scattering processes that take place in these experiments are governed by the electroweak force and the strong force. The strong force can be described by Quantum Chromodynamics, which exhibits complicated behavior in the low-energy regime.

The complicated nature of the strong force makes it difficult to derive intensity models from first principles. Instead, we have to rely on approximations given specific assumptions for the scattering process that we study. Each amplitude model that we formulate is almost always merely an approximation of the true scattering process. As a consequence, we always have to reassess our analysis results and try alternative models. In addition, amplitude models can be extremely complicated, with large, complex-valued parametrizations and dozens of input parameters. We therefore want to evaluate these models with as much information as possible. That means large input data samples and 'fits' using the full likelihood function.

Given these challenges, we can identify **three major requirements that amplitude analysis software should satisfy**:

:::{card} {material-regular}`speed` Performance
We want to evaluate likelihood function as fast as possible over large data samples, so that we can optimize our model parameters for several hypotheses.
:::

:::{card} {material-regular}`edit` Flexibility
We want to quickly formulate a wide range of amplitude models, given the latest theoretical and experimental insights.
:::

:::{card} {material-regular}`school` Transparency
It must be easy to understand the mathematics behind the implemented model, so that the analysis can be reproduced or compared to comparable experiments.
:::
