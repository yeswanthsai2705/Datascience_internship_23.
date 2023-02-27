import streamlit as st

st.title(":red[INNOMATICS] Data App")

st.header('This is a task for the internship')
st.subheader('Task is done in FEB 2023')




CODE = ''' print("hello world") '''
st.code(CODE, language='python')

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50,20),
    columns=('col %d' % i for i in range(20))
    )


st.dataframe(df)