import os
from solcx import install_solc

install_solc(version="latest")

from solcx.main import _compile_combined_json

compiled_fundme = _compile_combined_json(
    source_files="FundMe.sol",
    output_values=["abi", "bin"],
    base_path=os.getcwd(),
    include_path=f"{os.getcwd()}/node_modules",
)
