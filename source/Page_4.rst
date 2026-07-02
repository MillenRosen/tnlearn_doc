API Reference
===========================

+-----------------------------+-----------------------------------------+
| ``tnlearn.VecSymRegressor`` | Symbolic Regression with Regressor Class|
+-----------------------------+-----------------------------------------+
| ``tnlearn.MLPClassifier``   | MLPClassifier Class Implementation      |
+-----------------------------+-----------------------------------------+
| ``tnlearn.MLPRegressor``    | MLPRegressor Class Implementation       |
+-----------------------------+-----------------------------------------+
| ``tnlearn.LLMSymRegressor`` | LLM-based Symbolic Regression Class     |
+-----------------------------+-----------------------------------------+
| ``tnlearn.RLRegressor``     | Reinforcement Learning Regressor Class  |
+-----------------------------+-----------------------------------------+



.. role:: classtext
   :class: classtext


tnlearn.VecSymRegressor
-----------------------

- Description:
    ``tnlearn.VecSymRegressor`` implements the symbolic regression algorithm through the Regressor class, enabling the evolution of mathematical expressions to fit given data. The class provides methods for generating random expressions, evaluating their fitness, and evolving expressions through mutation and crossover. It aims to find the best-fitting mathematical model for a given dataset.

    .. container:: custom-background

       ``tnlearn.VecSymRegressor`` : :classtext:`class` **tnlearn.VecSymRegressor** :classtext:`(random_state=100, pop_size=5000, max_generations=20, tournament_size=10, x_pct=0.7, xover_pct=0.3, save=True, operations=None)`


- **How to initialize your** ``VecSymRegressor`` **:**
    ``random_state``：Seed for random number generation **(default: 100)**

    ``pop_size``：Population size for genetic algorithm **(default: 5000)**

    ``max_generations``：Maximum generations for genetic algorithm **(default: 20)**

    ``tournament_size``：Size of tournament selection **(default: 10)**

    ``x_pct``：Probability of selecting a variable node during random program generation **(default: 0.7)**

    ``xover_pct``：Crossover probability during offspring generation **(default: 0.3)**

    ``save``：Flag for saving **(default: False)**

        .. container:: custom-background-2

            **False:** Don't need to save the progress

            **True:** If save option is enabled, open a file called **"log.txt"** to log the progress

    ``operations``：Set of operations to be used in program generation **(default: None)**

        .. container:: custom-background-2

            **None:** Use the default mathematical operations for the algorithm, like the following code:

            .. code-block:: python
                :linenos:

                (
                {"func": operator.add, "arg_count": 2, "format_str": "({} + {})"},
                {"func": operator.sub, "arg_count": 2, "format_str": "({} - {})"},
                {"func": operator.mul, "arg_count": 2, "format_str": "({} * {})"},
                {"func": operator.neg, "arg_count": 1, "format_str": "-({})"},
                )

            You can also define ``operations`` in a similar way.



- **Here is an example of using** ``VecSymRegressor`` **quickly:**

    .. code-block:: text

        from tnlearn import Regressor

        >> neuron = Regressor()
        >> neuron.fit(X_train, y_label)
        >> print('*' * 20)
        >> print(neuron.neuron)

        ********************
        6@x**2 + 1.46@x - 0.1316

    .. note::
        Format ``X_train`` and ``y_label`` as **numpy arrays**.

        In the above example, the shapes of ``X_train`` and ``y_label`` are **(600, 10)** and **(600, 1)** respectively.



tnlearn.MLPClassifier
----------------------

- Description:
    ``tnlearn.MLPClassifier`` implements the class MLPClassifier, which extends the functionality of the base class to build and train a Multi-layer Perceptron (MLP) model. MLPClassifier is designed to allow easy customization of the neural network structure, activation functions, and loss function used during training. It incorporates device selection to leverage available GPU resources, ensuring efficient computation. The class covers essential methods for model training, evaluation, and prediction, making it a flexible tool for supervised learning tasks in PyTorch.

    .. container:: custom-background

       ``tnlearn.MLPClassifier`` : :classtext:`class` **tnlearn.MLPClassifier** :classtext:`(neurons='x', layers_list=None, activation_funcs=None, loss_function=None, optimizer_name='adam', random_state=1, max_iter=300, batch_size=128, valid_size=0.2, lr=0.01, visual=False, save=False, visual_interval=100, gpu=None, interval=None, scheduler=None, l1_reg=None, l2_reg=None)`


- **How to initialize your** ``tnlearn.MLPClassifier`` **:**
    ``neurons``: Neuronal expression **(default: 'x')**

        .. container:: custom-background-2

            Users can pass the results of ``tnlearn.VecSymRegressor`` to ``neurons``

    ``layers_list``: List of neuron counts for each hidden layer **(default: [50, 30, 10])**

    ``activation_funcs``: Activation functions **(default: None)**

        .. container:: custom-background-2

            Users can choose different activation functions: ``'relu'``, ``'leakyrelu'``, ``'sigmoid'``, ``'tanh'``,  ``'softmax'``

    ``loss_function``: Loss function for the training process **(default: None)**

        .. container:: custom-background-2

            Users can choose different loss functions: ``'mse'``, ``'l1'``, ``'crossentropy'``, ``'bce'``

    ``optimizer_name``: Name of the optimizer algorithm **(default: 'adam')**

        .. container:: custom-background-2

            Users can choose different optimizers: ``'adam'``, ``'sgd'``, ``'rmsprop'``, ``'adamw'``

    ``random_state``: Seed for random number generators for reproducibility **(default: 1)**

    ``max_iter``: Maximum number of training iterations **(default: 300)**

    ``batch_size``: Number of samples per batch during training **(default: 128)**

    ``valid_size``: Fraction of training data used for validation **(default: 0.2)**

    ``lr``: Learning rate for the optimizer **(default: 0.01)**

    ``visual``: Boolean indicating if training visualization is to be shown **(default: False)**

    ``save``: Indicates if the training figure should be saved **(default: False)**

    ``visual_interval``: Interval at which training visualization is updated **(default: 100)**

    ``gpu``: Specifies GPU configuration for training **(default: None)**

        .. container:: custom-background-2

            **None**: Not use GPU

            **An Integer (e.g. 1)**: How many GPUs you want to use

    ``interval``: Interval of screen output during training **(default: None)**

    ``scheduler``: Learning rate scheduler **(default: None)**

        .. container:: custom-background-2

            **None**:  Not use any learning rate adjustment strategy

            **{'step_size': 30, 'gamma': 0.2}**:  Use ``lr_sceduler.StepLR()`` with **"step_size = 30"** and **"gamma = 0.2"**

    ``l1_reg``: L1 regularization term **(default: None)**

        .. container:: custom-background-2

            **None**:  Not use L1 regularization

            **True**:  Use L1 regularization

    ``l2_reg``: L2 regularization term **(default: None)**

        .. container:: custom-background-2

            **None**:  Not use L2 regularization

            **True**:  Use L2 regularization


- **Here is an example of using** ``MLPClassifier`` **quickly:**

    .. code-block:: python
        :linenos:

        from tnlearn import MLPClassifier
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        from tnlearn import VecSymRegressor

        X, y = make_classification(n_samples=200, random_state=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

        neuron = VecSymRegressor()

        neuron.fit(X_train, y_train)
        print('*' * 20)
        print(neuron.neuron)

        layers_list = [10, 10, 10]
        clf = MLPClassifier()

        clf.fit(X_train, y_train)
        print(f"Score: {clf.score(X_test, y_test)}")

        clf.save(path='my_model_dir', filename='mlp_classifier.pth')
        clf.load(path='my_model_dir', filename='mlp_classifier.pth', input_dim=X_train.shape[1], output_dim=1)
        clf.fit(X_train, y_train)


tnlearn.MLPRegressor
--------------------

- Description:
    ``tnlearn.MLPRegressor`` embodies the MLPRegressor class, designed as an extension of BaseModel within a custom machine learning framework. It facilitates the creation and training of a multilayer perceptron (MLP) for regression tasks. Features of the class include the flexibility to define custom neural network architectures through parameters such as neuronal expression and layer structure, the utilization of various activation functions, and the incorporation of modern optimization algorithms and regularization techniques. Moreover, the class is equipped with optional GPU support for enhanced computational efficiency, as well as functionalities for training visualization, validation, and model performance evaluation. This representation of an MLP is tailored to adapt to an array of regression problems while ensuring ease of use and extensibility.

    .. container:: custom-background

       ``tnlearn.MLPRegressor`` : :classtext:`class` **tnlearn.MLPRegressor** :classtext:`(neurons='x', layers_list=None, activation_funcs=None, loss_function=None, optimizer_name='adam', random_state=1, max_iter=300, batch_size=128, valid_size=0.2, lr=0.01, visual=False, save=False, visual_interval=100, gpu=None, interval=None, scheduler=None, l1_reg=None, l2_reg=None)`


- **How to initialize your** ``tnlearn.MLPRegressor`` **:**
    ``neurons``: Neuronal expression **(default: 'x')**

        .. container:: custom-background-2

            Users can pass the results of ``tnlearn.VecSymRegressor`` to ``neurons``

    ``layers_list``: List of neuron counts for each hidden layer **(default: [50, 30, 10])**

    ``activation_funcs``: Activation functions **(default: None)**

        .. container:: custom-background-2

            Users can choose different activation functions: ``'relu'``, ``'leakyrelu'``, ``'sigmoid'``, ``'tanh'``,  ``'softmax'``

    ``loss_function``: Loss function for the training process **(default: None)**

        .. container:: custom-background-2

            Users can choose different loss functions: ``'mse'``, ``'l1'``, ``'crossentropy'``, ``'bce'``

    ``optimizer_name``: Name of the optimizer algorithm **(default: 'adam')**

        .. container:: custom-background-2

            Users can choose different optimizers: ``'adam'``, ``'sgd'``, ``'rmsprop'``, ``'adamw'``

    ``random_state``: Seed for random number generators for reproducibility **(default: 1)**

    ``max_iter``: Maximum number of training iterations **(default: 300)**

    ``batch_size``: Number of samples per batch during training **(default: 128)**

    ``valid_size``: Fraction of training data used for validation **(default: 0.2)**

    ``lr``: Learning rate for the optimizer **(default: 0.01)**

    ``visual``: Boolean indicating if training visualization is to be shown **(default: False)**

    ``save``: Indicates if the training figure should be saved **(default: False)**

    ``visual_interval``: Interval at which training visualization is updated **(default: 100)**

    ``gpu``: Specifies GPU configuration for training **(default: None)**

        .. container:: custom-background-2

            **None**: Not use GPU

            **An Integer (e.g. 1)**: How many GPUs you want to use

    ``interval``: Interval of screen output during training **(default: None)**

    ``scheduler``: Learning rate scheduler **(default: None)**

        .. container:: custom-background-2

            **None**:  Not use any learning rate adjustment strategy

            **{'step_size': 30, 'gamma': 0.2}**:  Use ``lr_sceduler.StepLR()`` with **"step_size = 30"** and **"gamma = 0.2"**

    ``l1_reg``: L1 regularization term **(default: None)**

        .. container:: custom-background-2

            **None**:  Not use L1 regularization

            **True**:  Use L1 regularization

    ``l2_reg``: L2 regularization term **(default: None)**

        .. container:: custom-background-2

            **None**:  Not use L2 regularization

            **True**:  Use L2 regularization


- **Here is an example of using** ``MLPRegressor`` **quickly:**

    .. code-block:: python
        :linenos:

        from tnlearn import MLPRegressor
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        from tnlearn import VecSymRegressor

        X, y = make_classification(n_samples=200, random_state=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

        neuron = VecSymRegressor()

        neuron.fit(X_train, y_train)
        print('*' * 20)
        print(neuron.neuron)

        layers_list = [10, 10, 10]
        clf = MLPRegressor()

        clf.fit(X_train, y_train)
        print(f"Score: {clf.score(X_test, y_test)}")

        clf.save(path='my_model_dir', filename='mlp_regressor.pth')
        clf.load(path='my_model_dir', filename='mlp_regressor.pth', input_dim=X_train.shape[1], output_dim=1)
        clf.fit(X_train, y_train)


tnlearn.LLMSymRegressor
-----------------------

- Description:
    ``tnlearn.LLMSymRegressor`` implements an LLM-based symbolic regression agent. It combines LLM‑generated equation skeletons with numerical optimization to discover interpretable expressions. The discovered expression can be directly used as a neuron formula in ``MLPRegressor``. The agent supports multiple LLM providers (DeepSeek, SiliconFlow, Ollama, BLT, CSTCloud) and uses an experience replay buffer to iteratively improve candidate equations.

    .. container:: custom-background

       ``tnlearn.LLMSymRegressor`` : :classtext:`class` **tnlearn.LLMSymRegressor** :classtext:`(llm_config=None, max_iterations=20, samples_per_iteration=8, background=None, verbose=True, max_params=10, n_restarts=5, bfgs_maxiter=200, extra_prompt=None, exp_dir=None, save=False, random_state=None)`

- **How to initialize your** ``LLMSymRegressor`` **:**

    ``llm_config``: Dictionary configuring the LLM provider **(default: None)**

        .. container:: custom-background-2

            Must contain a ``model`` key in the format ``'provider/model'``, e.g. ``'deepseek/deepseek-chat'``.  
            Optional keys: ``'api_key'`` (string or dict), ``'base_url'``, ``'temperature'`` (float, default 0.6), ``'max_tokens'`` (int, default 1024), ``'top_p'`` (float, default 0.3).  
            If no ``api_key`` is given, the corresponding environment variable is used (e.g. ``DEEPSEEK_API_KEY``, ``SILICONFLOW_API_KEY``).

    ``max_iterations``: Number of evolutionary iterations (rounds of LLM sampling + evaluation) **(default: 20)**

    ``samples_per_iteration``: Number of candidate equations generated per iteration **(default: 8)**

    ``background``: Optional physical background description to guide the LLM **(default: None)**

    ``verbose``: Verbosity level. If int: 0=quiet, 1=basic progress, 2=detailed debug; if bool: True -> 1, False -> 0 **(default: True)**

    ``max_params``: Maximum number of coefficients (``params``) allowed in the equation **(default: 10)**

    ``n_restarts``: Number of multi‑start BFGS runs used during evaluation **(default: 5)**

    ``bfgs_maxiter``: Maximum BFGS iterations per optimization run **(default: 200)**

    ``extra_prompt``: Additional user-provided text appended to the LLM prompt after the equation template **(default: None)**

    ``exp_dir``: Directory for saving experiment logs and the best equation (if ``save=True``). If not given and ``save=False``, no folder is created **(default: None)**

    ``save``: If ``True``, save experiment logs and the best equation to ``exp_dir``; if ``False``, keep everything in memory **(default: False)**

    ``random_state``: Seed for random number generators for reproducibility **(default: None)**

- **Supported LLM Providers**

    The following provider strings are recognised in the ``model`` field (case‑insensitive):

    .. list-table::
       :header-rows: 1
       :widths: auto

       * - Provider
         - Example ``model``
         - Environment variable for API key
       * - DeepSeek
         - ``deepseek/deepseek-chat``
         - ``DEEPSEEK_API_KEY``
       * - SiliconFlow
         - ``siliconflow/Qwen/Qwen3-8B``
         - ``SILICONFLOW_API_KEY``
       * - Ollama (local)
         - ``ollama/llama3.1:8b``
         - (not required)
       * - BLT
         - ``blt/gpt-4``
         - ``BLT_API_KEY``
       * - CSTCloud
         - ``cstcloud/gpt-oss-120b``
         - ``CSTCLOUD_API_KEY``

- **Attributes after fitting**

    After calling ``fit()``, the following attributes are available:

    - ``best_equation_``: the best discovered equation body (a string starting with ``return ...``).
    - ``best_score_``: the highest negative MSE (the evaluation score, higher = better).
    - ``best_params_``: a numpy array of optimized coefficients for ``params[0]``, ``params[1]``, ….
    - The method ``get_neuron_formula()`` returns a string with numeric coefficients, ready to be used as the ``neurons`` argument in ``MLPRegressor``.

- **Here is an example of using** ``LLMSymRegressor`` **quickly:**

    .. code-block:: python
        :linenos:

        from tnlearn import LLMSymRegressor, MLPRegressor
        from sklearn.datasets import make_regression
        from sklearn.model_selection import train_test_split

        X, y = make_regression(n_samples=200, random_state=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

        llm_config = {'model': 'deepseek/deepseek-chat'}   # set DEEPSEEK_API_KEY environment variable

        neuron = LLMSymRegressor(llm_config=llm_config, max_iterations=5)
        neuron.fit(X_train, y_train)

        clf = MLPRegressor(neurons=reg.get_neuron_formula(), layers_list=[50,30,10])
        clf.fit(X_train, y_train)
        clf.predict(X_test)

    .. note::
        The ``fit`` method automatically performs BFGS parameter optimization. The resulting formula from ``get_neuron_formula()`` contains a numeric expression (e.g. ``3.0@x**2 + 2.0@x + 0.1``) that can be passed directly to the ``neurons`` parameter of ``MLPRegressor``.

tnlearn.RLRegressor
-------------------

- Description:
    ``tnlearn.RLRegressor`` implements a reinforcement learning (policy gradient) agent that discovers a **vectorized (homogeneous) symbolic expression** of the form:

    .. math::

        f(\mathbf{x}) = b + \sum_{k} c_k \sum_{j=1}^{d} \phi_k(x_j)

    where :math:`\mathbf{x} \in \mathbb{R}^d` is a multi‑feature input vector, :math:`b` is an intercept, :math:`\phi_k` are basis functions selected from a user‑defined set, and :math:`c_k` are coefficients fitted via Ridge regression. The agent learns to select a subset of basis functions (up to ``max_terms``) to maximise the validation R². The discovered expression can be directly used as a neuron formula in ``MLPRegressor``.

    .. container:: custom-background

       ``tnlearn.RLRegressor`` : :classtext:`class` **tnlearn.RLRegressor** :classtext:`(basis_mode='trigonometric', max_terms=3, max_power=5, alpha=0.1, random_state=42, max_episodes=100, val_split=0.2, lr_rl=1e-3, gamma=0.99, hidden_dim=64, verbose=True)`

- **How to initialize your** ``RLRegressor`` **:**

    ``basis_mode`` : determines the set of available basis functions **(default: 'trigonometric')**

        .. container:: custom-background-2

            - ``'polynomial'`` : only polynomials (constant, :math:`x`, :math:`x^2`, …, :math:`x^{\text{max_power}}`)
            - ``'trigonometric'`` : polynomials plus :math:`\sin(x)` and :math:`\cos(x)`
            - ``'all'`` : polynomials plus :math:`\sin(x)`, :math:`\cos(x)`, :math:`\exp(x)`, and :math:`\log(|x|)` (with a small safety offset)

    ``max_terms`` : maximum number of basis functions allowed in the expression **(default: 3)**

    ``max_power`` : maximum exponent for polynomial terms (i.e., :math:`x^2` to :math:`x^{\text{max_power}}`). The linear term :math:`x` and the constant are always available **(default: 5)**

    ``alpha`` : regularisation strength for Ridge regression **(default: 0.1)**

    ``random_state`` : random seed for reproducibility **(default: 42)**

    ``max_episodes`` : number of training episodes **(default: 100)**

    ``val_split`` : fraction of training data used as validation for reward computation **(default: 0.2)**

    ``lr_rl`` : learning rate for the policy network **(default: 1e-3)**

    ``gamma`` : discount factor for reward calculation **(default: 0.99)**

    ``hidden_dim`` : number of neurons in the policy network's hidden layers **(default: 64)**

    ``verbose`` : if ``True``, print progress updates during training **(default: True)**

- **Supported basis functions** (depending on ``basis_mode``)

    - **Polynomial terms** (always available): constant (implicit via intercept), :math:`x`, :math:`x^2`, …, :math:`x^{\text{max_power}}`
    - **Trigonometric terms** (if ``basis_mode`` is ``'trigonometric'`` or ``'all'``): :math:`\sin(x)`, :math:`\cos(x)`
    - **Exponential/Logarithmic** (only in ``'all'`` mode): :math:`\exp(x)`, :math:`\log(|x| + 1e-8)`

- **Attributes after fitting**

    - ``best_expr`` : the best discovered symbolic expression (with numeric coefficients and intercept), e.g., ``"0.01 + 2.01@(x**2) + 2.99@x + 0.48@(sin(x))"``.
    - ``best_score`` : the best validation R² score achieved.
    - ``neuron`` : alias for ``best_expr``, compatible with the ``neurons`` parameter of ``MLPRegressor``.

- **Here is an example of using** ``RLRegressor`` **quickly:**

    .. code-block:: python
        :linenos:

        from tnlearn import RLRegressor, MLPRegressor
        import numpy as np
        from sklearn.model_selection import train_test_split

        # Generate multi‑feature data with a homogeneous pattern
        np.random.seed(42)
        X = np.random.uniform(-2, 2, (500, 3))
        y = 2.0 * np.sum(X**2, axis=1) + 3.0 * np.sum(X, axis=1) + 0.5 * np.sum(np.sin(X), axis=1)
        y += 0.1 * np.random.randn(500)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        rl = RLRegressor(basis_mode='trigonometric', max_terms=4, max_episodes=150, verbose=True)
        rl.fit(X_train, y_train)

        expr = rl.get_neuron()
        mlp = MLPRegressor(neurons=expr, layers_list=[30,20])
        mlp.fit(X_train, y_train)
        mlp.predict(X_test)

    .. warning::
        When ``basis_mode='all'``, terms like ``exp(x)`` and ``log(x)`` may cause numerical instability for large inputs. Ensure your data is appropriately scaled.

tnlearn.modules – Task‑based Neural Modules
============================================

The ``tnlearn.modules`` subpackage provides a family of neural network layers that extend standard PyTorch layers (linear, convolutional, and recurrent) by allowing the user to specify a **symbolic expression** as the neuron's aggregation function. This enables the construction of task‑specific neurons directly within popular architectures.

All modules follow a unified mathematical framework: the input (or hidden state) is transformed by a set of user‑defined basis functions :math:`f_i`, and the results are linearly combined with learnable weights :math:`W_i`:

.. math::

   \text{output} = \sum_{i} W_i \cdot f_i(\text{input}) + b

where :math:`\cdot` denotes the appropriate linear operation (matrix multiplication, convolution, or transposed convolution). Each basis function has its own learnable weight, providing both flexibility and interpretability.

**Example of symbolic expression interpretation**

Suppose you set ``symbolic_expression = '2@x + 4@x**3 + torch.sin(x)'``. This indicates the use of three basis functions:

- :math:`f_1(x) = x`
- :math:`f_2(x) = x^3`
- :math:`f_3(x) = \sin(x)`

The layer will learn three weight matrices :math:`W_1, W_2, W_3` (or convolution kernels) and compute:

.. math::

   \text{output} = W_1 \cdot x + W_2 \cdot x^3 + W_3 \cdot \sin(x) + b

where :math:`x` is the input tensor. All operations (:math:`x`, :math:`x^3`, :math:`\sin(x)`) are **element‑wise** over the input features (or spatial dimensions for convolutions). The coefficients ``2@`` and ``4@`` are ignored because the layer learns its own weights; they are only for parsing convenience.

.. contents:: :local:


TNLinear
--------

.. container:: custom-background

   ``tnlearn.modules.TNLinear`` : :classtext:`class` **TNLinear** :classtext:`(in_features, out_features, symbolic_expression='x', bias=True, device=None, dtype=None)`

- Description:
    A custom **fully‑connected layer with task‑based neurons**, where the neuron's aggregation function is defined by a symbolic expression. The input is first transformed by each basis function in the expression, and the results are linearly combined with learnable weights:

    .. math::

       y = \sum_{i} W_i \, f_i(x) + b

    The coefficients (e.g., ``3@`` and ``4@`` in ``'3@x + 4@x**3 + torch.sin(x)'``) are **ignored**; the layer learns its own weight for each basis function. When ``symbolic_expression='x'``, this layer reduces to a standard affine transformation (equivalent to ``nn.Linear``).

    This module supports TensorFloat32.

- **Parameters**

    .. container:: custom-background-2

        ``in_features`` : size of each input sample **(default: required)**

        ``out_features`` : size of each output sample **(default: required)**

        ``symbolic_expression`` : string defining the basis functions, e.g., ``'x + torch.sin(x) + x**3'`` or ``'3@x + 4@x**3 + torch.sin(x)'``. The variable ``x`` represents the input. The layer learns its own weights for each basis function, so numeric coefficients are ignored. **(default: 'x')**

        ``bias`` : If set to ``False``, the layer will not learn an additive bias. **(default: True)**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(*, H_{in})` where :math:`H_{in} = \text{in_features}` and :math:`*` means any number of dimensions.
    - Output: :math:`(*, H_{out})` where all but the last dimension are the same shape as the input and :math:`H_{out} = \text{out_features}`.

- **Variables**

    - ``weight`` : the learnable weights of the module of shape :math:`(\text{out_features}, \text{in_features})` per basis function. Initialized from :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where :math:`k = \frac{1}{\text{in_features}}`.
    - ``bias`` : the learnable bias of the module of shape :math:`(\text{out_features})`. If ``bias`` is ``True``, initialized from :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where :math:`k = \frac{1}{\text{in_features}}`.

- **Examples**

    .. code-block:: python

        from tnlearn import TNLinear
        import torch

        # Example 1: using multiple basis functions
        m1 = TNLinear(20, 30, symbolic_expression='x + torch.sin(x)')
        input1 = torch.randn(128, 20)
        output1 = m1(input1)

        # Example 2: using a symbolic expression with coefficients (ignored)
        m2 = TNLinear(20, 30, symbolic_expression='3@x + 4@x**3 + torch.sin(x)')
        input2 = torch.randn(128, 20)
        output2 = m2(input2)
        print(output2.size())   # torch.Size([128, 30])


TNConv1d
--------

.. container:: custom-background

   ``tnlearn.modules.TNConv1d`` : :classtext:`class` **TNConv1d** :classtext:`(in_channels, out_channels, kernel_size, stride=1, padding=0, symbolic_expression='x', groups=1, dilation=1, padding_mode='zeros', bias=True, device=None, dtype=None)`

- Description:
    Applies a 1D convolution over an input signal composed of several input planes, where the input is first transformed by a set of basis functions defined by ``symbolic_expression``:

    .. math::

       \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) + \sum_{k=0}^{C_{\text{in}}-1} \sum_{m} W_m \star f_m(\text{input}(N_i, k))

    where :math:`\star` is the valid cross-correlation operator, and :math:`f_m` are the basis functions.

    All parameters are identical to those of :class:`torch.nn.Conv1d`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``in_channels`` : number of channels in the input image **(default: required)**

        ``out_channels`` : number of channels produced by the convolution **(default: required)**

        ``kernel_size`` : size of the convolving kernel **(default: required)**

        ``stride`` : stride of the convolution **(default: 1)**

        ``padding`` : padding added to both sides of the input **(default: 0)**

        ``symbolic_expression`` : basis functions to apply element‑wise to the input (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``groups`` : number of blocked connections from input channels to output channels **(default: 1)**

        ``dilation`` : spacing between kernel elements **(default: 1)**

        ``padding_mode`` : ``'zeros'``, ``'reflect'``, ``'replicate'`` or ``'circular'`` **(default: 'zeros')**

        ``bias`` : if ``True``, adds a learnable bias to the output **(default: True)**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, C_{in}, L_{in})`
    - Output: :math:`(N, C_{out}, L_{out})` where

      .. math::

         \begin{aligned}
         L_{out} = \Big\lfloor & \frac{L_{in} + 2 \times \text{padding} - \text{dilation} \times (\text{kernel_size} - 1) - 1}{\text{stride}} \Big\rfloor + 1
         \end{aligned}

- **Example**

    .. code-block:: python

        from tnlearn import TNConv1d
        import torch

        m = TNConv1d(16, 33, 3, stride=2, symbolic_expression='x + torch.sin(x)')
        input = torch.randn(20, 16, 50)
        output = m(input)


TNConv2d
--------

.. container:: custom-background

   ``tnlearn.modules.TNConv2d`` : :classtext:`class` **TNConv2d** :classtext:`(in_channels, out_channels, kernel_size, stride=1, padding=0, symbolic_expression='x', groups=1, dilation=1, padding_mode='zeros', bias=True, device=None, dtype=None)`

- Description:
    Applies a 2D convolution over an input signal composed of several input planes, where the input is first transformed by a set of basis functions defined by ``symbolic_expression``:

    .. math::

       \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) + \sum_{k=0}^{C_{\text{in}}-1} \sum_{m} W_m \star f_m(\text{input}(N_i, k))

    where :math:`\star` is the valid 2D cross-correlation operator, and :math:`f_m` are the basis functions.

    All parameters are identical to those of :class:`torch.nn.Conv2d`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``in_channels`` : number of channels in the input image **(default: required)**

        ``out_channels`` : number of channels produced by the convolution **(default: required)**

        ``kernel_size`` : size of the convolving kernel **(default: required)**

        ``stride`` : stride of the convolution **(default: 1)**

        ``padding`` : padding added to all four sides of the input **(default: 0)**

        ``symbolic_expression`` : basis functions to apply element‑wise to the input (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``groups`` : number of blocked connections from input channels to output channels **(default: 1)**

        ``dilation`` : spacing between kernel elements **(default: 1)**

        ``padding_mode`` : ``'zeros'``, ``'reflect'``, ``'replicate'`` or ``'circular'`` **(default: 'zeros')**

        ``bias`` : if ``True``, adds a learnable bias to the output **(default: True)**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, C_{in}, H_{in}, W_{in})`
    - Output: :math:`(N, C_{out}, H_{out}, W_{out})` where

      .. math::

         \begin{aligned}
         H_{out} = \Big\lfloor & \frac{H_{in} + 2 \times \text{padding}[0] - \text{dilation}[0] \times (\text{kernel_size}[0] - 1) - 1}{\text{stride}[0]} \Big\rfloor + 1
         \end{aligned}

      .. math::

         \begin{aligned}
         W_{out} = \Big\lfloor & \frac{W_{in} + 2 \times \text{padding}[1] - \text{dilation}[1] \times (\text{kernel_size}[1] - 1) - 1}{\text{stride}[1]} \Big\rfloor + 1
         \end{aligned}

- **Example**

    .. code-block:: python

        from tnlearn import TNConv2d
        import torch

        m = TNConv2d(16, 33, 3, stride=2, symbolic_expression='x + 0.5@x**2')
        input = torch.randn(20, 16, 50, 100)
        output = m(input)


TNConv3d
--------

.. container:: custom-background

   ``tnlearn.modules.TNConv3d`` : :classtext:`class` **TNConv3d** :classtext:`(in_channels, out_channels, kernel_size, stride=1, padding=0, symbolic_expression='x', groups=1, dilation=1, padding_mode='zeros', bias=True, device=None, dtype=None)`

- Description:
    Applies a 3D convolution over an input signal composed of several input planes, where the input is first transformed by a set of basis functions defined by ``symbolic_expression``:

    .. math::

       \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) + \sum_{k=0}^{C_{\text{in}}-1} \sum_{m} W_m \star f_m(\text{input}(N_i, k))

    where :math:`\star` is the valid 3D cross-correlation operator, and :math:`f_m` are the basis functions.

    All parameters are identical to those of :class:`torch.nn.Conv3d`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``in_channels`` : number of channels in the input image **(default: required)**

        ``out_channels`` : number of channels produced by the convolution **(default: required)**

        ``kernel_size`` : size of the convolving kernel **(default: required)**

        ``stride`` : stride of the convolution **(default: 1)**

        ``padding`` : padding added to all sides of the input **(default: 0)**

        ``symbolic_expression`` : basis functions to apply element‑wise to the input (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``groups`` : number of blocked connections from input channels to output channels **(default: 1)**

        ``dilation`` : spacing between kernel elements **(default: 1)**

        ``padding_mode`` : ``'zeros'``, ``'reflect'``, ``'replicate'`` or ``'circular'`` **(default: 'zeros')**

        ``bias`` : if ``True``, adds a learnable bias to the output **(default: True)**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, C_{in}, D_{in}, H_{in}, W_{in})`
    - Output: :math:`(N, C_{out}, D_{out}, H_{out}, W_{out})` where

      .. math::

         \begin{aligned}
         D_{out} = \Big\lfloor & \frac{D_{in} + 2 \times \text{padding}[0] - \text{dilation}[0] \times (\text{kernel_size}[0] - 1) - 1}{\text{stride}[0]} \Big\rfloor + 1
         \end{aligned}

      .. math::

         \begin{aligned}
         H_{out} = \Big\lfloor & \frac{H_{in} + 2 \times \text{padding}[1] - \text{dilation}[1] \times (\text{kernel_size}[1] - 1) - 1}{\text{stride}[1]} \Big\rfloor + 1
         \end{aligned}

      .. math::

         \begin{aligned}
         W_{out} = \Big\lfloor & \frac{W_{in} + 2 \times \text{padding}[2] - \text{dilation}[2] \times (\text{kernel_size}[2] - 1) - 1}{\text{stride}[2]} \Big\rfloor + 1
         \end{aligned}

- **Example**

    .. code-block:: python

        from tnlearn import TNConv3d
        import torch

        m = TNConv3d(16, 33, 3, stride=2, symbolic_expression='x + torch.cos(x)')
        input = torch.randn(20, 16, 10, 50, 100)
        output = m(input)


TNConvTranspose1d
-----------------

.. container:: custom-background

   ``tnlearn.modules.TNConvTranspose1d`` : :classtext:`class` **TNConvTranspose1d** :classtext:`(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, symbolic_expression='x', groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)`

- Description:
    Applies a 1D transposed convolution operator over an input signal composed of several input planes, where the input is first transformed by a set of basis functions defined by ``symbolic_expression``:

    .. math::

       \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) + \sum_{k=0}^{C_{\text{in}}-1} \sum_{m} W_m \circledast f_m(\text{input}(N_i, k))

    where :math:`\circledast` is the transposed convolution operator, and :math:`f_m` are the basis functions.

    All parameters are identical to those of :class:`torch.nn.ConvTranspose1d`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``in_channels`` : number of channels in the input image **(default: required)**

        ``out_channels`` : number of channels produced by the convolution **(default: required)**

        ``kernel_size`` : size of the convolving kernel **(default: required)**

        ``stride`` : stride of the convolution **(default: 1)**

        ``padding`` : ``dilation * (kernel_size - 1) - padding`` zero-padding will be added to both sides of the input **(default: 0)**

        ``output_padding`` : additional size added to one side of the output shape **(default: 0)**

        ``symbolic_expression`` : basis functions to apply element‑wise to the input (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``groups`` : number of blocked connections from input channels to output channels **(default: 1)**

        ``bias`` : if ``True``, adds a learnable bias to the output **(default: True)**

        ``dilation`` : spacing between kernel elements **(default: 1)**

        ``padding_mode`` : ``'zeros'``, ``'reflect'``, ``'replicate'`` or ``'circular'`` **(default: 'zeros')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, C_{in}, L_{in})`
    - Output: :math:`(N, C_{out}, L_{out})` where

      .. math::

         \begin{aligned}
         L_{out} = &(L_{in} - 1) \times \text{stride} - 2 \times \text{padding} \\
                   &+ \text{dilation} \times (\text{kernel_size} - 1) + \text{output_padding} + 1
         \end{aligned}

- **Example**

    .. code-block:: python

        from tnlearn import TNConvTranspose1d
        import torch

        m = TNConvTranspose1d(16, 33, 3, stride=2, symbolic_expression='x**2')
        input = torch.randn(20, 16, 50)
        output = m(input)


TNConvTranspose2d
-----------------

.. container:: custom-background

   ``tnlearn.modules.TNConvTranspose2d`` : :classtext:`class` **TNConvTranspose2d** :classtext:`(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, symbolic_expression='x', groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)`

- Description:
    Applies a 2D transposed convolution operator over an input signal composed of several input planes, where the input is first transformed by a set of basis functions defined by ``symbolic_expression``:

    .. math::

       \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) + \sum_{k=0}^{C_{\text{in}}-1} \sum_{m} W_m \circledast f_m(\text{input}(N_i, k))

    where :math:`\circledast` is the transposed convolution operator, and :math:`f_m` are the basis functions.

    All parameters are identical to those of :class:`torch.nn.ConvTranspose2d`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``in_channels`` : number of channels in the input image **(default: required)**

        ``out_channels`` : number of channels produced by the convolution **(default: required)**

        ``kernel_size`` : size of the convolving kernel **(default: required)**

        ``stride`` : stride of the convolution **(default: 1)**

        ``padding`` : ``dilation * (kernel_size - 1) - padding`` zero-padding will be added to both sides of each spatial dimension **(default: 0)**

        ``output_padding`` : additional size added to one side of each spatial dimension of the output shape **(default: 0)**

        ``symbolic_expression`` : basis functions to apply element‑wise to the input (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``groups`` : number of blocked connections from input channels to output channels **(default: 1)**

        ``bias`` : if ``True``, adds a learnable bias to the output **(default: True)**

        ``dilation`` : spacing between kernel elements **(default: 1)**

        ``padding_mode`` : ``'zeros'``, ``'reflect'``, ``'replicate'`` or ``'circular'`` **(default: 'zeros')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, C_{in}, H_{in}, W_{in})`
    - Output: :math:`(N, C_{out}, H_{out}, W_{out})` where

      .. math::

         \begin{aligned}
         H_{out} = &(H_{in} - 1) \times \text{stride}[0] - 2 \times \text{padding}[0] \\
                   &+ \text{dilation}[0] \times (\text{kernel_size}[0] - 1) + \text{output_padding}[0] + 1
         \end{aligned}

      .. math::

         \begin{aligned}
         W_{out} = &(W_{in} - 1) \times \text{stride}[1] - 2 \times \text{padding}[1] \\
                   &+ \text{dilation}[1] \times (\text{kernel_size}[1] - 1) + \text{output_padding}[1] + 1
         \end{aligned}

- **Example**

    .. code-block:: python

        from tnlearn import TNConvTranspose2d
        import torch

        m = TNConvTranspose2d(16, 33, 3, stride=2, symbolic_expression='x + torch.sin(x)')
        input = torch.randn(20, 16, 50, 100)
        output = m(input)


TNConvTranspose3d
-----------------

.. container:: custom-background

   ``tnlearn.modules.TNConvTranspose3d`` : :classtext:`class` **TNConvTranspose3d** :classtext:`(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, symbolic_expression='x', groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)`

- Description:
    Applies a 3D transposed convolution operator over an input signal composed of several input planes, where the input is first transformed by a set of basis functions defined by ``symbolic_expression``:

    .. math::

       \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) + \sum_{k=0}^{C_{\text{in}}-1} \sum_{m} W_m \circledast f_m(\text{input}(N_i, k))

    where :math:`\circledast` is the transposed convolution operator, and :math:`f_m` are the basis functions.

    All parameters are identical to those of :class:`torch.nn.ConvTranspose3d`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``in_channels`` : number of channels in the input image **(default: required)**

        ``out_channels`` : number of channels produced by the convolution **(default: required)**

        ``kernel_size`` : size of the convolving kernel **(default: required)**

        ``stride`` : stride of the convolution **(default: 1)**

        ``padding`` : ``dilation * (kernel_size - 1) - padding`` zero-padding will be added to both sides of each spatial dimension **(default: 0)**

        ``output_padding`` : additional size added to one side of each spatial dimension of the output shape **(default: 0)**

        ``symbolic_expression`` : basis functions to apply element‑wise to the input (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``groups`` : number of blocked connections from input channels to output channels **(default: 1)**

        ``bias`` : if ``True``, adds a learnable bias to the output **(default: True)**

        ``dilation`` : spacing between kernel elements **(default: 1)**

        ``padding_mode`` : ``'zeros'``, ``'reflect'``, ``'replicate'`` or ``'circular'`` **(default: 'zeros')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, C_{in}, D_{in}, H_{in}, W_{in})`
    - Output: :math:`(N, C_{out}, D_{out}, H_{out}, W_{out})` where

      .. math::

         \begin{aligned}
         D_{out} = &(D_{in} - 1) \times \text{stride}[0] - 2 \times \text{padding}[0] \\
                   &+ \text{dilation}[0] \times (\text{kernel_size}[0] - 1) + \text{output_padding}[0] + 1
         \end{aligned}

      .. math::

         \begin{aligned}
         H_{out} = &(H_{in} - 1) \times \text{stride}[1] - 2 \times \text{padding}[1] \\
                   &+ \text{dilation}[1] \times (\text{kernel_size}[1] - 1) + \text{output_padding}[1] + 1
         \end{aligned}

      .. math::

         \begin{aligned}
         W_{out} = &(W_{in} - 1) \times \text{stride}[2] - 2 \times \text{padding}[2] \\
                   &+ \text{dilation}[2] \times (\text{kernel_size}[2] - 1) + \text{output_padding}[2] + 1
         \end{aligned}

- **Example**

    .. code-block:: python

        from tnlearn import TNConvTranspose3d
        import torch

        m = TNConvTranspose3d(16, 33, 3, stride=2, symbolic_expression='x**2 + torch.cos(x)')
        input = torch.randn(20, 16, 10, 50, 100)
        output = m(input)


TNRNN
-----

.. container:: custom-background

   ``tnlearn.modules.TNRNN`` : :classtext:`class` **TNRNN** :classtext:`(input_size, hidden_size, num_layers=1, nonlinearity='tanh', bias=True, batch_first=False, dropout=0.0, bidirectional=False, symbolic_expression='x', device=None, dtype=None)`

- Description:
    Applies a multi-layer Elman RNN with :math:`\tanh` or :math:`\text{ReLU}` non-linearity to an input sequence, where both the input‑to‑hidden and hidden‑to‑hidden transformations are augmented with basis functions defined by ``symbolic_expression``.

    For each element in the input sequence, each layer computes:

    .. math::

       h_t = \text{act}\!\left( \sum_{i} W_{ih}^{(i)} f_i(x_t) + \sum_{j} W_{hh}^{(j)} f_j(h_{t-1}) + b \right)

    where :math:`f_i` and :math:`f_j` are the basis functions derived from ``symbolic_expression``, applied to the input and the previous hidden state respectively. The layer learns separate weight matrices for each basis function.

    All parameters are identical to those of :class:`torch.nn.RNN`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``input_size`` : the number of expected features in the input :math:`x` **(default: required)**

        ``hidden_size`` : the number of features in the hidden state :math:`h` **(default: required)**

        ``num_layers`` : number of recurrent layers **(default: 1)**

        ``nonlinearity`` : the non-linearity to use. Can be either ``'tanh'`` or ``'relu'``. **(default: 'tanh')**

        ``bias`` : if ``False``, the layer does not use bias weights **(default: True)**

        ``batch_first`` : if ``True``, input and output tensors are provided as ``(batch, seq, feature)`` **(default: False)**

        ``dropout`` : if non-zero, introduces a Dropout layer on the outputs of each RNN layer except the last layer **(default: 0.0)**

        ``bidirectional`` : if ``True``, becomes a bidirectional RNN **(default: False)**

        ``symbolic_expression`` : symbolic expression defining the basis functions for both input and hidden transformations (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Example**

    .. code-block:: python

        from tnlearn import TNRNN
        import torch

        rnn = TNRNN(10, 20, 2, symbolic_expression='x + torch.sin(x)')
        input = torch.randn(5, 3, 10)
        h0 = torch.randn(2, 3, 20)
        output, hn = rnn(input, h0)


TNLSTM
------

.. container:: custom-background

   ``tnlearn.modules.TNLSTM`` : :classtext:`class` **TNLSTM** :classtext:`(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, symbolic_expression='x', device=None, dtype=None)`

- Description:
    Applies a multi-layer long short-term memory (LSTM) RNN to an input sequence, where the input‑to‑hidden and hidden‑to‑hidden transformations are augmented with basis functions defined by ``symbolic_expression``.

    For each element in the input sequence, each layer computes the LSTM equations with basis functions replacing the linear transformations.

    All parameters are identical to those of :class:`torch.nn.LSTM`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``input_size`` : the number of expected features in the input :math:`x` **(default: required)**

        ``hidden_size`` : the number of features in the hidden state :math:`h` **(default: required)**

        ``num_layers`` : number of recurrent layers **(default: 1)**

        ``bias`` : if ``False``, the layer does not use bias weights **(default: True)**

        ``batch_first`` : if ``True``, input and output tensors are provided as ``(batch, seq, feature)`` **(default: False)**

        ``dropout`` : if non-zero, introduces a Dropout layer on the outputs of each LSTM layer except the last layer **(default: 0.0)**

        ``bidirectional`` : if ``True``, becomes a bidirectional LSTM **(default: False)**

        ``symbolic_expression`` : symbolic expression defining the basis functions (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Example**

    .. code-block:: python

        from tnlearn import TNLSTM
        import torch

        lstm = TNLSTM(10, 20, 2, symbolic_expression='x + 0.5@x**2')
        input = torch.randn(5, 3, 10)
        h0 = torch.randn(2, 3, 20)
        c0 = torch.randn(2, 3, 20)
        output, (hn, cn) = lstm(input, (h0, c0))


TNGRU
-----

.. container:: custom-background

   ``tnlearn.modules.TNGRU`` : :classtext:`class` **TNGRU** :classtext:`(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, symbolic_expression='x', device=None, dtype=None)`

- Description:
    Applies a multi-layer gated recurrent unit (GRU) RNN to an input sequence, where the input‑to‑hidden and hidden‑to‑hidden transformations are augmented with basis functions defined by ``symbolic_expression``.

    For each element in the input sequence, each layer computes the GRU equations with basis functions replacing the linear transformations.

    All parameters are identical to those of :class:`torch.nn.GRU`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``input_size`` : the number of expected features in the input :math:`x` **(default: required)**

        ``hidden_size`` : the number of features in the hidden state :math:`h` **(default: required)**

        ``num_layers`` : number of recurrent layers **(default: 1)**

        ``bias`` : if ``False``, the layer does not use bias weights **(default: True)**

        ``batch_first`` : if ``True``, input and output tensors are provided as ``(batch, seq, feature)`` **(default: False)**

        ``dropout`` : if non-zero, introduces a Dropout layer on the outputs of each GRU layer except the last layer **(default: 0.0)**

        ``bidirectional`` : if ``True``, becomes a bidirectional GRU **(default: False)**

        ``symbolic_expression`` : symbolic expression defining the basis functions (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Example**

    .. code-block:: python

        from tnlearn import TNGRU
        import torch

        gru = TNGRU(10, 20, 2, symbolic_expression='x + torch.sin(x)')
        input = torch.randn(5, 3, 10)
        h0 = torch.randn(2, 3, 20)
        output, hn = gru(input, h0)


TNRNNCell
---------

.. container:: custom-background

   ``tnlearn.modules.TNRNNCell`` : :classtext:`class` **TNRNNCell** :classtext:`(input_size, hidden_size, bias=True, nonlinearity='tanh', symbolic_expression='x', device=None, dtype=None)`

- Description:
    An Elman RNN cell with :math:`\tanh` or :math:`\text{ReLU}` non-linearity, where both input‑to‑hidden and hidden‑to‑hidden transformations are augmented with basis functions defined by ``symbolic_expression``.

    This is the single‑step version of :class:`TNRNN`.

    All parameters are identical to those of :class:`torch.nn.RNNCell`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``input_size`` : the number of expected features in the input :math:`x` **(default: required)**

        ``hidden_size`` : the number of features in the hidden state :math:`h` **(default: required)**

        ``bias`` : if ``False``, the layer does not use bias weights **(default: True)**

        ``nonlinearity`` : the non-linearity to use. Can be either ``'tanh'`` or ``'relu'``. **(default: 'tanh')**

        ``symbolic_expression`` : symbolic expression defining the basis functions (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, H_{in})` or :math:`(H_{in})` where :math:`H_{in} = \text{input_size}`
    - Hidden: :math:`(N, H_{out})` or :math:`(H_{out})` where :math:`H_{out} = \text{hidden_size}` (defaults to zero if not provided)
    - Output: :math:`(N, H_{out})` or :math:`(H_{out})` tensor containing the next hidden state

- **Example**

    .. code-block:: python

        from tnlearn import TNRNNCell
        import torch

        rnn = TNRNNCell(10, 20, symbolic_expression='x + torch.sin(x)')
        input = torch.randn(6, 3, 10)
        hx = torch.randn(3, 20)
        output = []
        for i in range(6):
            hx = rnn(input[i], hx)
            output.append(hx)


TNLSTMCell
----------

.. container:: custom-background

   ``tnlearn.modules.TNLSTMCell`` : :classtext:`class` **TNLSTMCell** :classtext:`(input_size, hidden_size, bias=True, symbolic_expression='x', device=None, dtype=None)`

- Description:
    A long short-term memory (LSTM) cell, where input‑to‑hidden and hidden‑to‑hidden transformations are augmented with basis functions defined by ``symbolic_expression``.

    This is the single‑step version of :class:`TNLSTM`.

    All parameters are identical to those of :class:`torch.nn.LSTMCell`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``input_size`` : the number of expected features in the input :math:`x` **(default: required)**

        ``hidden_size`` : the number of features in the hidden state :math:`h` **(default: required)**

        ``bias`` : if ``False``, the layer does not use bias weights **(default: True)**

        ``symbolic_expression`` : symbolic expression defining the basis functions (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, H_{in})` or :math:`(H_{in})` where :math:`H_{in} = \text{input_size}`
    - Hidden: :math:`(N, H_{out})` or :math:`(H_{out})`, Cell: :math:`(N, H_{out})` or :math:`(H_{out})` where :math:`H_{out} = \text{hidden_size}` (defaults to zero if not provided)
    - Output: :math:`(h', c')` each of shape :math:`(N, H_{out})` or :math:`(H_{out})`

- **Example**

    .. code-block:: python

        from tnlearn import TNLSTMCell
        import torch

        rnn = TNLSTMCell(10, 20, symbolic_expression='x + 0.1@x**2')
        input = torch.randn(6, 3, 10)
        hx = torch.randn(3, 20)
        cx = torch.randn(3, 20)
        output = []
        for i in range(6):
            hx, cx = rnn(input[i], (hx, cx))
            output.append(hx)


TNGRUCell
---------

.. container:: custom-background

   ``tnlearn.modules.TNGRUCell`` : :classtext:`class` **TNGRUCell** :classtext:`(input_size, hidden_size, bias=True, symbolic_expression='x', device=None, dtype=None)`

- Description:
    A gated recurrent unit (GRU) cell, where input‑to‑hidden and hidden‑to‑hidden transformations are augmented with basis functions defined by ``symbolic_expression``.

    This is the single‑step version of :class:`TNGRU`.

    All parameters are identical to those of :class:`torch.nn.GRUCell`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``input_size`` : the number of expected features in the input :math:`x` **(default: required)**

        ``hidden_size`` : the number of features in the hidden state :math:`h` **(default: required)**

        ``bias`` : if ``False``, the layer does not use bias weights **(default: True)**

        ``symbolic_expression`` : symbolic expression defining the basis functions (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(N, H_{in})` or :math:`(H_{in})` where :math:`H_{in} = \text{input_size}`
    - Hidden: :math:`(N, H_{out})` or :math:`(H_{out})` where :math:`H_{out} = \text{hidden_size}` (defaults to zero if not provided)
    - Output: :math:`(N, H_{out})` or :math:`(H_{out})` tensor containing the next hidden state

- **Example**

    .. code-block:: python

        from tnlearn import TNGRUCell
        import torch

        rnn = TNGRUCell(10, 20, symbolic_expression='x + torch.cos(x)')
        input = torch.randn(6, 3, 10)
        hx = torch.randn(3, 20)
        output = []
        for i in range(6):
            hx = rnn(input[i], hx)
            output.append(hx)



TNTransformer
-------------

.. container:: custom-background

   ``tnlearn.modules.TNTransformer`` : :classtext:`class` **TNTransformer** :classtext:`(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048, dropout=0.1, activation='relu', custom_encoder=None, custom_decoder=None, layer_norm_eps=1e-5, batch_first=False, norm_first=False, bias=True, symbolic_expression='x', device=None, dtype=None)`

- Description:
    A basic Transformer model where the feed‑forward networks and linear projections in encoder/decoder layers are replaced with :class:`TNLinear`, allowing user‑defined basis functions (e.g., ``'x + torch.sin(x)'``) inside the transformer blocks.

    This module implements the original Transformer architecture described in the *Attention Is All You Need* paper. The intent of this layer is as a reference implementation for foundational understanding and thus it contains only limited features relative to newer Transformer architectures. All parameters are identical to those of :class:`torch.nn.Transformer`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``d_model`` : the number of expected features in the encoder/decoder inputs **(default: 512)**

        ``nhead`` : the number of heads in the multiheadattention models **(default: 8)**

        ``num_encoder_layers`` : the number of sub‑encoder‑layers in the encoder **(default: 6)**

        ``num_decoder_layers`` : the number of sub‑decoder‑layers in the decoder **(default: 6)**

        ``dim_feedforward`` : the dimension of the feedforward network model **(default: 2048)**

        ``dropout`` : the dropout value **(default: 0.1)**

        ``activation`` : the activation function of encoder/decoder intermediate layer, can be a string (``'relu'`` or ``'gelu'``) or a unary callable **(default: 'relu')**

        ``custom_encoder`` : custom encoder **(default: None)**

        ``custom_decoder`` : custom decoder **(default: None)**

        ``layer_norm_eps`` : the eps value in layer normalization components **(default: 1e-5)**

        ``batch_first`` : if ``True``, input and output tensors are provided as ``(batch, seq, feature)`` **(default: False)**

        ``norm_first`` : if ``True``, layer norm is done prior to attention and feedforward operations **(default: False)**

        ``bias`` : if set to ``False``, ``Linear`` and ``LayerNorm`` layers will not learn an additive bias **(default: True)**

        ``symbolic_expression`` : symbolic expression defining the basis functions for all :class:`TNLinear` layers inside the transformer (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Example**

    .. code-block:: python

        from tnlearn import TNTransformer
        import torch

        transformer = TNTransformer(
            d_model=512, nhead=8,
            num_encoder_layers=2, num_decoder_layers=2,
            symbolic_expression='x + torch.tanh(x)'
        )
        src = torch.randn(10, 32, 512)   # (seq, batch, feature)
        tgt = torch.randn(20, 32, 512)
        out = transformer(src, tgt)

    .. note::
        This class uses :class:`TNTransformerEncoder` and :class:`TNTransformerDecoder` internally. When `batch_first=False` (default), the input and output shapes are `(seq, batch, feature)`. When `batch_first=True`, shapes are `(batch, seq, feature)`.


TNTransformerEncoder
--------------------

.. container:: custom-background

   ``tnlearn.modules.TNTransformerEncoder`` : :classtext:`class` **TNTransformerEncoder** :classtext:`(encoder_layer, num_layers, norm=None, enable_nested_tensor=True, mask_check=True)`

- Description:
    A stack of N encoder layers, where each layer uses :class:`TNTransformerEncoderLayer`. This module is the TNLearn counterpart of :class:`torch.nn.TransformerEncoder`.

    TransformerEncoder is a stack of N encoder layers. The intent of this layer is as a reference implementation for foundational understanding.

    .. warning::
        All layers in the TransformerEncoder are initialized with the same parameters. It is recommended to manually initialize the layers after creating the TransformerEncoder instance.

- **Parameters**

    .. container:: custom-background-2

        ``encoder_layer`` : an instance of the :class:`TNTransformerEncoderLayer` class **(required)**

        ``num_layers`` : the number of sub‑encoder‑layers in the encoder **(required)**

        ``norm`` : the layer normalization component **(optional)**

        ``enable_nested_tensor`` : if ``True``, input will automatically convert to nested tensor (and convert back on output). This will improve the overall performance when padding rate is high **(default: True)**

        ``mask_check`` : whether to check the mask for left‑aligned padding **(default: True)**

- **Example**

    .. code-block:: python

        from tnlearn import TNTransformerEncoderLayer, TNTransformerEncoder
        import torch

        encoder_layer = TNTransformerEncoderLayer(
            d_model=512, nhead=8,
            symbolic_expression='x + 0.5 * torch.sin(x)'
        )
        transformer_encoder = TNTransformerEncoder(encoder_layer, num_layers=2)
        src = torch.randn(10, 32, 512)
        out = transformer_encoder(src)


TNTransformerDecoder
--------------------

.. container:: custom-background

   ``tnlearn.modules.TNTransformerDecoder`` : :classtext:`class` **TNTransformerDecoder** :classtext:`(decoder_layer, num_layers, norm=None)`

- Description:
    A stack of N decoder layers, where each layer uses :class:`TNTransformerDecoderLayer`. This module is the TNLearn counterpart of :class:`torch.nn.TransformerDecoder`.

    TransformerDecoder is a stack of N decoder layers. The intent of this layer is as a reference implementation for foundational understanding.

    .. warning::
        All layers in the TransformerDecoder are initialized with the same parameters. It is recommended to manually initialize the layers after creating the TransformerDecoder instance.

- **Parameters**

    .. container:: custom-background-2

        ``decoder_layer`` : an instance of the :class:`TNTransformerDecoderLayer` class **(required)**

        ``num_layers`` : the number of sub‑decoder‑layers in the decoder **(required)**

        ``norm`` : the layer normalization component **(optional)**

- **Example**

    .. code-block:: python

        from tnlearn import TNTransformerDecoderLayer, TNTransformerDecoder
        import torch

        decoder_layer = TNTransformerDecoderLayer(
            d_model=512, nhead=8,
            symbolic_expression='x * torch.sigmoid(x)'
        )
        transformer_decoder = TNTransformerDecoder(decoder_layer, num_layers=2)
        tgt = torch.randn(20, 32, 512)
        memory = torch.randn(10, 32, 512)
        out = transformer_decoder(tgt, memory)


TNTransformerEncoderLayer
-------------------------

.. container:: custom-background

   ``tnlearn.modules.TNTransformerEncoderLayer`` : :classtext:`class` **TNTransformerEncoderLayer** :classtext:`(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-5, batch_first=False, norm_first=False, bias=True, symbolic_expression='x', device=None, dtype=None)`

- Description:
    TransformerEncoderLayer is made up of self‑attention and a feed‑forward network (FFN). The FFN uses :class:`TNLinear` to support custom basis functions defined by ``symbolic_expression``, while the self‑attention projections (query/key/value and output) remain as standard ``nn.Linear`` layers.

    This layer implements the original Transformer encoder block described in the *Attention Is All You Need* paper. All parameters are identical to those of :class:`torch.nn.TransformerEncoderLayer`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``d_model`` : the number of expected features in the input **(required)**

        ``nhead`` : the number of heads in the multiheadattention models **(required)**

        ``dim_feedforward`` : the dimension of the feedforward network model **(default: 2048)**

        ``dropout`` : the dropout value **(default: 0.1)**

        ``activation`` : the activation function of the intermediate layer, can be a string (``'relu'`` or ``'gelu'``) or a unary callable **(default: 'relu')**

        ``layer_norm_eps`` : the eps value in layer normalization components **(default: 1e-5)**

        ``batch_first`` : if ``True``, input and output tensors are provided as ``(batch, seq, feature)`` **(default: False)**

        ``norm_first`` : if ``True``, layer norm is done prior to self attention and feedforward operations **(default: False)**

        ``bias`` : if set to ``False``, ``Linear`` and ``LayerNorm`` layers will not learn an additive bias **(default: True)**

        ``symbolic_expression`` : symbolic expression defining the basis functions for the :class:`TNLinear` layers in the FFN (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: :math:`(S, N, E)` or :math:`(N, S, E)` if ``batch_first=True``, where :math:`S` is the source sequence length, :math:`N` is the batch size, and :math:`E` is the feature dimension.
    - Output: same shape as input.

- **Example**

    .. code-block:: python

        from tnlearn import TNTransformerEncoderLayer
        import torch

        encoder_layer = TNTransformerEncoderLayer(
            d_model=512, nhead=8,
            symbolic_expression='x + torch.sin(x)'
        )
        src = torch.randn(10, 32, 512)   # (seq, batch, feature)
        out = encoder_layer(src)


TNTransformerDecoderLayer
-------------------------

.. container:: custom-background

   ``tnlearn.modules.TNTransformerDecoderLayer`` : :classtext:`class` **TNTransformerDecoderLayer** :classtext:`(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-5, batch_first=False, norm_first=False, bias=True, symbolic_expression='x', device=None, dtype=None)`

- Description:
    TransformerDecoderLayer is made up of self‑attention, cross‑attention, and a feed‑forward network (FFN). The FFN uses :class:`TNLinear` to support custom basis functions defined by ``symbolic_expression``, while the attention projections (query/key/value and output) remain as standard ``nn.Linear`` layers.

    This layer implements the original Transformer decoder block described in the *Attention Is All You Need* paper. All parameters are identical to those of :class:`torch.nn.TransformerDecoderLayer`, with the addition of ``symbolic_expression``.

- **Parameters**

    .. container:: custom-background-2

        ``d_model`` : the number of expected features in the input **(required)**

        ``nhead`` : the number of heads in the multiheadattention models **(required)**

        ``dim_feedforward`` : the dimension of the feedforward network model **(default: 2048)**

        ``dropout`` : the dropout value **(default: 0.1)**

        ``activation`` : the activation function of the intermediate layer, can be a string (``'relu'`` or ``'gelu'``) or a unary callable **(default: 'relu')**

        ``layer_norm_eps`` : the eps value in layer normalization components **(default: 1e-5)**

        ``batch_first`` : if ``True``, input and output tensors are provided as ``(batch, seq, feature)`` **(default: False)**

        ``norm_first`` : if ``True``, layer norm is done prior to self attention, cross attention and feedforward operations **(default: False)**

        ``bias`` : if set to ``False``, ``Linear`` and ``LayerNorm`` layers will not learn an additive bias **(default: True)**

        ``symbolic_expression`` : symbolic expression defining the basis functions for the :class:`TNLinear` layers in the FFN (same syntax as :class:`TNLinear`) **(default: 'x')**

        ``device`` : the desired device of the parameters **(default: None)**

        ``dtype`` : the desired dtype of the parameters **(default: None)**

- **Shape**

    - Input: target :math:`(T, N, E)`, memory :math:`(S, N, E)` (or with batch first if enabled).
    - Output: same shape as target.

- **Example**

    .. code-block:: python

        from tnlearn import TNTransformerDecoderLayer
        import torch

        decoder_layer = TNTransformerDecoderLayer(
            d_model=512, nhead=8,
            symbolic_expression='x**2 + torch.cos(x)'
        )
        tgt = torch.randn(20, 32, 512)   # (tgt_seq, batch, feature)
        memory = torch.randn(10, 32, 512)
        out = decoder_layer(tgt, memory)

Common Notes
------------

- **Basis function syntax**: The expression is a Python string that can contain any valid PyTorch operations (e.g., ``torch.sin``, ``torch.cos``, ``torch.exp``, ``**``, ``*``, etc.). The variable representing the input is always ``x``. Coefficients (e.g., ``0.5@x**2``) are ignored because the layer learns its own weights; the ``@`` symbol is only used for parsing.

- **Weight sharing**: Each basis function :math:`f_i` has its own weight matrix/convolution kernel (or linear projection). Consequently, the number of trainable parameters scales linearly with the number of basis functions. This applies to all modules in ``tnlearn.modules``, including linear, convolutional, recurrent, and transformer layers.

- **Transformer-specific**: In transformer encoder/decoder layers, only the feed‑forward network (FFN) uses :class:`TNLinear`; the attention projections (query/key/value and output) remain standard `nn.Linear` layers for efficiency and stability.

- **Save/load**: All modules support standard PyTorch serialisation via :func:`torch.save` and :func:`torch.load`, including the dynamic function compilation.

- **Performance**: The forward pass evaluates each basis function in a loop. For large models or many basis functions, consider using simpler expressions to reduce computational and memory overhead.

- **Integration**: These modules are fully compatible with PyTorch's optimizers, data parallelism, and mixed precision training.

.. note::
   The RNN modules internally augment the input by concatenating the outputs of all basis functions along the feature dimension before passing to a native PyTorch RNN implementation. This provides high performance while still allowing arbitrary symbolic expressions.