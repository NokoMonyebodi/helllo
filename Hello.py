## Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import subprocess
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot 


# Install required packages
subprocess.run(['pip', 'install', 'matplotlib'])


# Sample data (replace this with your data)
data = {
    'Flux': [0.0635896, 0.06832498, 0.07357413, 0.079442389, 0.08693351, 0.09378168, 0.0285238, 0.0304512, 0.0326057,
             0.0351447, 0.0384098, 0.0411464, 0.0107654, 0.0115086, 0.0122346, 0.0133011, 0.0144021, 0.0154852, 0.07217133,
             0.07744611, 0.08228934, 0.08970974, 0.09717094, 0.1050358],
    'Frequency': [17.447, 16.423, 15.447, 14.423, 13.447, 12.423, 17.447, 16.423, 15.447, 14.423, 13.447, 12.423, 17.447,
                  16.423, 15.447, 14.423, 13.447, 12.423, 17.447, 16.423, 15.447, 14.423, 13.447, 12.423]
}

# Converting the data to a DataFrame
df = pd.DataFrame(data)

# Streamlit app begins here
st.title('Flux vs Frequency Plot')

# Plotting with Matplotlib
fig, ax = plt.subplots()
ax.plot(df['Frequency'][0:6], df['Flux'][0:6], "*", label='A2')
ax.plot(df['Frequency'][6:12], df['Flux'][6:12], "*", label='B')
ax.plot(df['Frequency'][12:18], df['Flux'][12:18], "*", label='C')
ax.plot(df['Frequency'][18:24], df['Flux'][18:24], "*", label='A1')

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("Frequency [GHz]")
ax.set_ylabel("Flux [Jy]")
ax.legend()

# Display the Matplotlib plot using st.pyplot
st.pyplot(fig)
