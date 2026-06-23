# -------------------------
# Produção de calor (W/kg of isotope)
# -------------------------
H_U238 = 9.46e-5
H_U235 = 5.69e-4
H_Th232 = 2.64e-5
H_K40  = 2.92e-5

# -------------------------
# Abundância no manto terrestre (kg/kg manto)
# -------------------------
C_U = 31.0E-9
C_Th = 124.0E-9
C_K  = 36.9E-9

# -------------------------
# funções de decaimento
# -------------------------
U238 = C_U * 0.9927 * np.exp(t * ln2 / tau_U238)
U235 = C_U * 0.0072 * np.exp(t * ln2 / tau_U235)
Th232 = C_Th * np.exp(t * ln2 / tau_Th232)
K40  = C_K  * np.exp(t * ln2 / tau_K40)

# -------------------------
# Produção de calor (W/kg)
# -------------------------
H = (
    U238 * H_U238 +
    U235 * H_U235 +
    Th232 * H_Th232 +
    K40  * H_K40
)
