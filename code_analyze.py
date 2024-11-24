import radon.raw as rr
import radon.metrics as rm
import radon.complexity as rc
import streamlit as st


class CodeAnalyze:
    def __init__(self, raw_code):
        self.raw_code = raw_code


    def analyze_code(self):
        st.subheader("RAW SCA Metrics")
        basic_analysis = rr.analyze(self.raw_code)
        st.write(basic_analysis)

    def metrics_calc(self):
       mi_results = round(rm.mi_visit(self.raw_code,True),3)
       cc_results = rc.cc_visit(self.raw_code)

       col1, col2 = st.columns(2)
       col1.metric(label="Maintiablity Index",value=mi_results)


    def hals_metrics(self):
        hal_results = rm.h_visit(self.raw_code)

        with st.expander("Halstead Metrics"):
            st.write(hal_results[0])


