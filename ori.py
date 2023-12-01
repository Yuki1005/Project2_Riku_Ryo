import streamlit as st
st.header("幸せ最適化")
blist = []
alist = list(range(1,31,1))
for i in range(len(alist)):
    n1 = st.sidebar.radio("{}".format(alist[i]),("A","B","C","D","E","F","G"),horizontal=True)
    blist.append(n1)
    
st.write(blist)