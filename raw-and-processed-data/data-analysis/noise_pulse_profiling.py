import matplotlib.pyplot as plt
from plot_hardware import plot_circuit_series

qubit = [12, 16, 20]

damping_noise = ['fourier_checking',
                  'graph_state',
                  'hidden_linear_function',
                  'iqp',
                  'quantum_volume',
                  'phase_estimation']


fourier_checking = [0.05328655242919922, 0.05523228645324707, 0.11886787414550781]
graph_state = [0.06038928031921387, 0.05713629722595215, 0.10975933074951172]
hidden_linear_function = [0.07265567779541016, 0.11040592193603516, 0.06953048706054688]
iqp = [0.08864378929138184, 0.08291220664978027, 0.07298707962036133]
quantum_volume = [0.06019949913024902, 0.07570600509643555, 0.06973075866699219]
phase_estimation = [0.03302001953125, 0.03224349021911621, 0.04004240036010742]

literal_damping_noise = [fourier_checking,
                         graph_state,
                         hidden_linear_function,
                         iqp,
                         quantum_volume,
                         phase_estimation]

plot_circuit_series("noise/damping_noise_profiles.png", qubit, damping_noise, literal_damping_noise)

depolarising_noise = ['fourier_checking',
                  'graph_state',
                  'hidden_linear_function',
                  'iqp',
                  'quantum_volume',
                  'phase_estimation']

fourier_checking = [0.004895448684692383, 0.010708093643188477, 0.3521573543548584]
graph_state = [0.007156848907470703, 0.005805492401123047, 0.006085872650146484]
hidden_linear_function = [0.005984306335449219, 0.005419731140136719, 0.011576652526855469]
iqp = [0.005495786666870117, 0.005492687225341797, 0.005217790603637695]
quantum_volume = [0.00456547737121582, 0.0046405792236328125, 0.005121469497680664]
phase_estimation = [0.0035953521728515625, 0.004235982894897461, 0.004595756530761719]

literal_depolarising_noise = [fourier_checking,
                              graph_state,
                              hidden_linear_function,
                              iqp,
                              quantum_volume,
                              phase_estimation]

plot_circuit_series("noise/depolarising_noise_profiles.png", qubit, depolarising_noise, literal_depolarising_noise)
