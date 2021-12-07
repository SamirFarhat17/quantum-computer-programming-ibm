import matplotlib.pyplot as plt


# Plotting function
def plot_circuit_series(filename, qubits, circuit_names, circuit_values):
    x = "qubits"
    y = "times"

    for i in range(0, len(circuit_names)):
        plt.plot(qubits, circuit_values[i], label=circuit_names[i])
    plt.legend()
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(filename)
    plt.show()


# Arithmetic circuits
qubit_count = [5, 15, 25]

arithmetic_circuits = ['integer_comparator',
                        'weighted_adder',
                        'quadratic_form',
                        'draper_qft_adder',
                        'cdkm_ripple_carry_adder',
                        'vbe_ripple_carry_adder',
                        'hrs_cum_mult',
                        'rgqft_mult']

integer_comparator = [0.0010612010955810547, 0.001676797866821289, 0.0011930465698242188]
weighted_adder = [0.0017216205596923828 , 0.002050638198852539, 0.00350638198852539]
quadratic_form = [0.0018048286437988281, 0.0027971267700195312, 0.004352092742919922]
draper_qft_adder = [0.001207113265991211, 0.0013000965118408203, 0.001245260238647461]
cdkm_ripple_carry_adder = [0.0012688636779785156, 0.0013000965118408203, 0.0012934207916259766]
vbe_ripple_carry_adder = [0.0013158321380615234, 0.0012612342834472656, 0.0012850761413574219]
hrs_cum_mult = [0.0011341571807861328, 0.0015254020690917969, 0.0016775131225585938]
rgqft_mult = [0.0010333061218261719, 0.0015435218811035156, 0.001659393310546875]

literal_arithmetic_circuits = [integer_comparator,
                                weighted_adder,
                                quadratic_form,
                                draper_qft_adder,
                                cdkm_ripple_carry_adder,
                                vbe_ripple_carry_adder,
                                hrs_cum_mult,
                                rgqft_mult]

# plot_circuit_series("arithmetic_circuits.png", qubit_count, arithmetic_circuits, literal_arithmetic_circuits)

# N-Local Circuits
n_local_circuits = ['qft',
                    'real_amplitudes',
                    'real_amplitudes_linear',
                    'efficient_su2',
                    'efficient_su2_linear',
                    'excitation_preserving',
                    'excitation_preserving_linear']

qft = [0.0010848045349121094, 0.0015265941619873047, 0.0016295909881591797]
real_amplitudes = [0.001638174057006836, 0.005030393600463867,  0.018168210983276367]
real_amplitudes_linear = [0.0014727115631103516, 0.0021986961364746094, 0.005446672439575195]
efficient_su2 = [0.004689931869506836, 0.0024759769439697266, 0.004689931869506836]
efficient_su2_linear = [0.0015637874603271484, 0.0028181076049804688, 0.0038862228393554688]
excitation_preserving = [0.006394624710083008, 0.008515695571899414,  0.01223440170288086]
excitation_preserving_linear = [0.0026192665100097656, 0.007058620452880859, 0.018657207489013672]

literal_n_local_circuits = [qft,
                            real_amplitudes,
                            real_amplitudes_linear,
                            efficient_su2,
                            efficient_su2_linear,
                            excitation_preserving,
                            excitation_preserving_linear]

# plot_circuit_series("n_local_circuits.png", qubit_count, n_local_circuits, literal_n_local_circuits)

# Particular Quantum Circuits
particular_circuits = ['fourier_checking',
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

# Probability Distribution Circuits
prob_distro_circuits = ['uniform_distribution',
                        'normal_distribution',
                        'log_normal_distribution']

uniform_distribution = [0.0016887187957763672, 0.0020978450775146484, 0.002228260040283203]
normal_distribution = [0.00185887187957763672, 0.001990978450775146484, 0.002128260040283203]
log_normal_distribution = [0.001488713672, 0.00150978484, 0.00183260040283203]

literal_prob_distro_circuits = [uniform_distribution,
                                normal_distribution,
                                log_normal_distribution]

#plot_circuit_series("prob_distro_circuits.png", qubit_count, prob_distro_circuits, literal_prob_distro_circuits)

# Standard Gates
standard_gates = ['barrier',
                  'mc_phase']

barrier = [0.0012595653533935547, 0.0013742446899414062, 0.0014445781707763672]
mc_phase = [0.004196882247924805, 0.005513191223144531, 0.007679939270019531]

literal_standard_gates = [barrier,
                          mc_phase]

#plot_circuit_series("standard_circuits.png", qubit_count, standard_gates, literal_standard_gates)

# Pauli-Rotational Circuits
pauli_rotational_gates = ['linear_pauli_rotations',
                          'poly_pauli_rotations',
                          'piecewise_lin_pauli_rotations',
                          'piecewise_poly_pauli_rotations']

linear_pauli_rotations = [0.001491546630859375, 0.001375436782836914, 0.0013492107391357422]
poly_pauli_rotations = [0.0015048980712890625, 0.0012645721435546875, 0.0012407302856445312]
piecewise_lin_pauli_rotations = [0.001405477523803711, 0.0012080669403076172, 0.0012476444244384766]
piecewise_poly_pauli_rotations = [0.0014634132385253906, 0.001199960708618164, 0.0012407302856445312]

literal_pauli_rotations = [linear_pauli_rotations,
                           poly_pauli_rotations,
                           piecewise_lin_pauli_rotations,
                           piecewise_poly_pauli_rotations]

#plot_circuit_series("pauli_rotational_circuits.png", qubit_count, pauli_rotational_gates, literal_pauli_rotations)

# Generalized Gates
generalized_gates = ['mcmt',
                     'mcmtv_chain',
                     'permutation',
                     'gms',
                     'gr',
                     'grx',
                     'gry',
                     'grz']

mcmt = [0.009045076370239258, 0.0098045076370239258, 0.019445076370239258]
mcmtv_chain = [0.006337165832519531, 0.05038142204284668, 0.06701445579528809]
permutation = [0.0020928382873535156, 0.0020303726196289062, 0.0020356178283691406]
gms = [0.006465911865234375, 0.018717050552368164, 0.03470110893249512]
gr = [0.001691579818725586, 0.0014040470123291016, 0.0014197826385498047]
grx = [0.0017206668853759766, 0.001476287841796875, 0.00144195556640625]
gry = [0.0017211437225341797, 0.0014541149139404297, 0.001438140869140625]
grz = [0.0026886463165283203, 0.0023097991943359375, 0.008872509002685547]


literal_generalized_gates = [mcmt,
                             mcmtv_chain,
                             permutation,
                             gms,
                             gr,
                             grx,
                             gry,
                             grz]

plot_circuit_series("circuits/generalized_gates.png", qubit_count, generalized_gates, literal_generalized_gates)
