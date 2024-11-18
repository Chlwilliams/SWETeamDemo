import streamlit as st

import radon.raw as rr
import radon.metrics as rm
import radon.complexity as rc


def main():
    st.title("Static Code Analysis App")

    with st.form(key="myform"):
        raw_code = st.text_area("Enter Code Here")
        submit_button = st.form_submit_button(label="Analyze")



    tab1, tab2, tab3, tab4 = st.tabs(["Code Analysis", "test", "test", "test"])

    if submit_button: 
        with tab1:
            st.subheader("Code Analysis")
            with st.expander("Orginal Code"):
                st.code(raw_code)
            st.subheader("RAW SCA Metrics")
            basic_analysis = rr.analyze(raw_code)
            st.write(basic_analysis)

            mi_results = rm.mi_visit(raw_code,True)


            cc_results = rc.cc_visit(raw_code)
            #st.write(cc_results[0])

            hal_results = rm.h_visit(raw_code)

            col1, col2 = st.columns(2)
            col1.metric(label="Maintiablity Index",value=mi_results)
            col2.metric(label="Cyclomatic complexity",value=f"{cc_results[0]}")

            with st.expander("Halstead Metrics"):
                st.write(hal_results[0])

                

    


if __name__ == "__main__":
    main()