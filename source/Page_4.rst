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
    ``tnlearn.LLMSymRegressor`` implements an LLM-based symbolic regression agent. It combines large language model (LLM) generated equation skeletons with gradient‑free numerical optimization to discover interpretable mathematical expressions from data. The agent supports multiple LLM providers (DeepSeek, SiliconFlow, Ollama, BLT, CSTCloud) and uses an experience replay buffer to iteratively improve candidate equations.

    .. container:: custom-background

       ``tnlearn.LLMSymRegressor`` : :classtext:`class` **tnlearn.LLMSymRegressor** :classtext:`(llm_config=None, max_iterations=20, samples_per_iteration=8, background=None, random_state=None, verbose=True, extra_prompt=None)`

- **How to initialize your** ``LLMSymRegressor`` **:**
    ``llm_config``: Dictionary configuring the LLM provider **(default: None)**

        .. container:: custom-background-2

            Must contain a ``model`` key in the format ``'provider/model'``, e.g. ``'deepseek/deepseek-chat'``.  
            Optional keys: ``'api_key'`` (string or dict), ``'base_url'``, ``'temperature'`` (float, default 0.6), ``'max_tokens'`` (int, default 1024), ``'top_p'`` (float, default 0.3).  
            If no ``api_key`` is given, the corresponding environment variable is used (e.g. ``DEEPSEEK_API_KEY``, ``SILICONFLOW_API_KEY``).

    ``max_iterations``: Number of evolutionary iterations (rounds of LLM sampling + evaluation) **(default: 20)**

    ``samples_per_iteration``: Number of candidate equations generated per iteration **(default: 8)**

    ``background``: Optional physical background description to guide the LLM **(default: None)**

    ``random_state``: Seed for random number generators for reproducibility **(default: None)**

    ``verbose``: Verbosity level. If int: 0=quiet, 1=basic progress, 2=detailed debug; if bool: True -> 1, False -> 0 **(default: True)**

    ``extra_prompt``: Additional user-provided text appended to the prompt after the equation template **(default: None)**

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
    - ``best_params_``: a numpy array of optimized coefficients for ``params[0]``, ``params[1]``, etc.

- **Here is an example of using** ``LLMSymRegressor`` **quickly:**

    .. code-block:: python
        :linenos:

        from tnlearn import LLMSymRegressor
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import r2_score

        # Generate synthetic data: y = 3*x0 + 0.5*sin(x1) + noise
        np.random.seed(42)
        X = np.random.randn(200, 2)
        y = 3*X[:,0] + 0.5*np.sin(X[:,1]) + 0.1*np.random.randn(200)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # Configure LLM (set DEEPSEEK_API_KEY environment variable)
        llm_config = {'model': 'deepseek/deepseek-chat', 'temperature': 0.6}

        reg = LLMSymRegressor(llm_config=llm_config, max_iterations=5, verbose=1)
        reg.fit(X_train, y_train)

        print("Best equation body:")
        print(reg.best_equation_)
        # Example output: "return params[0]*x0 + params[1]*np.sin(x1) + params[2]"

        y_pred = reg.predict(X_test)
        print(f"Test R²: {r2_score(y_test, y_pred):.4f}")

        # Save and load the model
        reg.save(path='my_model_dir', filename='llmsym_regressor.pth')
        reg.load(path='my_model_dir', filename='llmsym_regressor.pth',
                 input_dim=X_train.shape[1], output_dim=1)

    .. note::
        The ``fit`` method automatically performs parameter optimization (BFGS) on the discovered equation.  
        The returned equation body uses placeholder parameters ``params[0]``, ``params[1]``, … which are replaced by the optimized values when calling ``predict``.

        For more advanced usage (e.g., customising the prompt or using a different LLM provider), refer to the online documentation.


tnlearn.RLRegressor
-------------------

- Description:
    ``tnlearn.RLRegressor`` implements a reinforcement learning (policy gradient) agent that selects a subset of basis functions (polynomials and optionally trigonometric terms) to form a symbolic expression. The agent explores the space of basis function combinations and uses Ridge regression to fit coefficients on the training set. The reward is the validation R² score. The discovered expression can be directly used as a neuron formula in MLPRegressor.

    .. container:: custom-background

       ``tnlearn.RLRegressor`` : :classtext:`class` **tnlearn.RLRegressor** :classtext:`(max_power=3, max_terms=5, max_freq=2, use_trigonometric=True, alpha=0.1, force_constant=True, random_state=42, max_episodes=100, val_split=0.2, lr_rl=1e-3, gamma=0.99, hidden_dim=64, verbose=True)`

- **How to initialize your** ``RLRegressor`` **:**
    ``max_power``: Maximum exponent for polynomial terms (x**p) **(default: 3)**

    ``max_terms``: Maximum number of basis functions selected per expression **(default: 5)**

    ``max_freq``: Maximum integer frequency for trigonometric functions (k in sin(k*x)) **(default: 2)**

    ``use_trigonometric``: Whether to include sin(k*x), cos(k*x) and their products as candidates **(default: True)**

    ``alpha``: Regularisation strength for Ridge regression **(default: 0.1)**

    ``force_constant``: If True, the constant term (1) is always included **(default: True)**

    ``random_state``: Random seed for reproducibility **(default: 42)**

    ``max_episodes``: Number of training episodes **(default: 100)**

    ``val_split``: Fraction of training data used as validation for reward computation **(default: 0.2)**

    ``lr_rl``: Learning rate for the policy network **(default: 1e-3)**

    ``gamma``: Discount factor for reward calculation **(default: 0.99)**

    ``hidden_dim``: Number of neurons in the policy network's hidden layers **(default: 64)**

    ``verbose``: If True, print progress updates during training **(default: True)**

- **Supported operators and functions**

    The basis functions include:

    - **Polynomial terms**: ``x**p`` (p = 1..max_power)
    - **Trigonometric terms** (if enabled): ``torch.sin(k*x)``, ``torch.cos(k*x)``, and their products with powers of x and with each other.
    - **Constant term** (always forced if ``force_constant=True``)

- **Attributes after fitting**

    - ``best_expr``: the best discovered symbolic expression (with numeric coefficients).
    - ``best_score``: the best validation R² score achieved.
    - ``neuron``: alias for ``best_expr``, compatible with MLPRegressor.

- **Here is an example of using** ``RLRegressor`` **quickly:**

    .. code-block:: python
        :linenos:

        from tnlearn import RLRegressor
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import r2_score

        # Generate synthetic univariate data: y = 2.5 * x**2 + 1.2*sin(2*x) + noise
        np.random.seed(42)
        X = np.random.uniform(-3, 3, 300).reshape(-1, 1)
        y = 2.5 * X[:,0]**2 + 1.2 * np.sin(2 * X[:,0]) + 0.05 * np.random.randn(300)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        reg = RLRegressor(max_episodes=200, max_terms=4, use_trigonometric=True, verbose=True)
        reg.fit(X_train, y_train)

        print("Best discovered expression:")
        print(reg.get_neuron())   # e.g., "2.50@x**2 + 1.20@torch.sin(2*x) + 0.05"

        y_pred = reg.predict(X_test)
        print(f"Test R²: {r2_score(y_test, y_pred):.4f}")

        # Use the discovered neuron in MLPRegressor
        from tnlearn import MLPRegressor
        mlp = MLPRegressor(neurons=reg.get_neuron(), layers_list=[30,20])
        mlp.fit(X_train, y_train)

    .. warning::
        The current implementation of ``RLRegressor`` only supports **univariate** regression (one input feature). Multivariate inputs will raise an error.

    .. note::
        The discovered expression uses ``@`` to separate coefficient and function, which is directly compatible with the ``neurons`` parameter of ``MLPRegressor``.  
        The trigonometric functions are expressed as ``torch.sin(...)`` and ``torch.cos(...)``, ensuring seamless integration with PyTorch.