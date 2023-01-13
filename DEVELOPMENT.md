This documents how to create the `requirements.txt` for this repository. You only need to be worried about this if you want to update the Jupyter Notebooks using new libraries. For just consuming the notebooks, refer to the [README.md](./README.md) which documents how to set up a virtual environment and make use of the existing `requirements.txt`.

## Setup environment and create requirements.txt

```bash
# create virtual environment
virtualenv env-jupyter2kibana

# activate (macOS)
source env-jupyter2kibana/bin/activate

# activate (Windows)
.\env-jupyter2kibana\Scripts\activate

# install notebook dependencies (example)
pip install pandas altair eland matplotlib numpy

# install kernel for jupyter notebooks
pip install ipykernel
python -m ipykernel install --user --name=env-jupyter2kibana

# create requirements.txt
pip freeze > requirements.txt

#deactivate once done
deactivate
```
