import matplotlib.pyplot as plt
from plot_hardware import plot_circuit_series

noise_qubit = [12, 16, 20]

noise_circuits = ['fourier_checking',
                  'graph_state',
                  'hidden_linear_function',
                  'iqp',
                  'quantum_volume',
                  'phase_estimation']


fourier_checking = [0.001523733139038086, 0.003541231155395508, 0.007541231155395508]
graph_state = [0.0015609264373779297, 0.0013730525970458984, 0.0013060569763183594]
hidden_linear_function = [0.001886129379272461, 0.0012502670288085938, 0.0012717247009277344]
iqp = [0.002405881881713867, 0.005211830139160156, 0.013214826583862305]
quantum_volume = [0.0018541812896728516, 0.0016889572143554688, 0.0023360252380371094]
phase_estimation = [0.0023887157440185547, 0.0009195804595947266, 0.0013735294342041016]

literal_particular_circuits = [fourier_checking,
                               graph_state,
                               hidden_linear_function,
                               iqp,
                               quantum_volume,
                               phase_estimation]

# plot_circuit_series("particular_circuits.png", qubit_count, particular_circuits, literal_particular_circuits)