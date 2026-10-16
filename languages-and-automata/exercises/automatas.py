from automata.fa.dfa import DFA

# # AFD 1: cadenas de 0 y 1 con longitud >= 4
# dfa1 = DFA(
#     states={"q0", "q1", "q2", "q3", "q4"},
#     input_symbols={"0", "1"},
#     transitions={
#         "q0": {"0": "q1", "1": "q1"},
#         "q1": {"0": "q2", "1": "q2"},
#         "q2": {"0": "q3", "1": "q3"},
#         "q3": {"0": "q4", "1": "q4"},
#         "q4": {"0": "q4", "1": "q4"},
#     },
#     initial_state="q0",
#     final_states={"q4"},
# )

# AFD 2: cadenas de la forma 10(10)*
dfa2 = DFA(
    states={"q0", "q1", "q2", "q3", "trampa"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"1": "q1", "0": "trampa"},
        "q1": {"0": "q2", "1": "trampa"},
        "q2": {"1": "q3", "0": "trampa"},
        "q3": {"0": "q2", "1": "trampa"},
        "trampa": {"0": "trampa", "1": "trampa"},
    },
    initial_state="q0",
    final_states={"q2"},
)


def probar(nombre, dfa, validas, invalidas):
    print(nombre)
    for cadena in validas:
        print(f"  '{cadena}' -> {dfa.accepts_input(cadena)} (esperado True)")
    for cadena in invalidas:
        print(f"  '{cadena}' -> {dfa.accepts_input(cadena)} (esperado False)")


# probar("AFD 1 (longitud >= 4)", dfa1,
#        ["0000", "0101", "1111", "10110", "000000"],
#        ["", "0", "01", "101", "110"])

probar(
    "AFD 2 (10(10)*)",
    dfa2,
    ["10", "1010", "101010", "10101010", "1010101010"],
    ["", "1", "11", "101", "100"],
)
