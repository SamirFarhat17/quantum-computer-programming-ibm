from qiskit.circuit.library import IntegerComparator, WeightedAdder, QuadraticForm

from benchmark.simulator_benchmark import SimulatorBenchmarkSuite


class BasicSimulatorBenchmarkSuite(SimulatorBenchmarkSuite):

    def __init__(self,
                 name='basic',
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=None,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = []
        if measure_counts is None:
            measure_counts = []
        if measures is None:
            measures = []
        if runtime_names is None:
            runtime_names = []
        if apps is None:
            apps = []
        if qubits is None:
            qubits = []

        super().__init__(name,
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)

    '''def track_statevector(self, app, measure, measure_count, noise_name, qubit):
        return self._run(self.RUNTIME_STATEVECTOR_CPU, app, measure, measure_count, noise_name, qubit)

    def track_matrix_product_state(self, app, measure, measure_count, noise_name, qubit):
        return self._run(self.RUNTIME_MPS_CPU, app, measure, measure_count, noise_name, qubit)'''
