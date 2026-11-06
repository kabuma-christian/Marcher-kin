import streamlit as st

st.set_page_config(page_title="Marché Facile", page_icon="🛒")

st.title("🛒 Marché Facile")
st.write("Calcule vite, sans erreur - Pour les vendeuses de Kinshasa")

nom = st.text_input("Nom du client", placeholder="Ex: Mama Sarah")
qt = st.number_input("Quantité", min_value=0, step=1)
prix = st.number_input("Prix unitaire (CDF)", min_value=0, step=100)
donne = st.number_input("Montant donné par le client (CDF)", min_value=0, step=500)

if st.button("CALCULER"):
    if qt == 0 or prix == 0:
        st.warning("Remplis la quantité et le prix d'abord")
    else:
        montant = qt * prix
        if montant > 10000:
            red = montant * 0.05
            net = montant - red
            st.success(f"Félicitations {nom} ! Réduction 5% : -{int(red)} CDF")
        else:
            red = 0
            net = montant
        
        st.info(f"Total : {int(montant)} CDF - À payer : {int(net)} CDF")

        if donne > 0:
            monnaie = donne - net
            if monnaie < 0:
                st.error(f"Il manque {-int(monnaie)} CDF, le client doit compléter")
            else:
                st.success(f"Monnaie à rendre : {int(monnaie)} CDF")
