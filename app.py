import streamlit as st
import os
import openai
api_key = (st.secrets["db"])
openai.api_key = api_key

st.title('Thirdweb Python SDK Code generator')

discovery_doc = "disc.json"

query = st.text_area("Describe the app you want to create: ")
ok = st.button("Generate Code")
if ok:
    response = openai.Completion.create(
    engine="davinci-codex",
    prompt="## Write code using thirdweb SDK to print all current NFTs and then mint a new NFT to a different address on the polygon mainnet.\n#\nfrom nftlabs import NftlabsSdk, SdkOptions, MintArg\nsdk = NftlabsSdk(SdkOptions(), \"https://polygon-rpc.com\")\nsdk.set_private_key(\"your private key here\")\nnft_module = sdk.get_nft_module(\"your thirdweb nft module key from dashboard\")\nprint(nft_module.get_all())\nprint(nft_module.mint_to(\"receivers address\", MintArg(name=\"name\", description=\"desc\",image_uri=\"add url\", properties={})))\n\"\"\"\"\"\"\n## Write code using the thirdweb SDK to mint 5 coins of a new currency and then transfer 2 coins to a different address. use polygon mainnet.\n#\nfrom nftlabs import NftlabsSdk, SdkOptions\nsdk = NftlabsSdk(SdkOptions(), \"https://polygon-rpc.com\")\nsdk.set_private_key(\"your private key here\")\ncurrency_module = sdk.get_currency_module(\"your thirdweb currency module key from dashboard\")\ncurrency_module.mint(5 * 10 ** 18)\ncurrency_module.transfer_from('senders address', 'receivers address', 2 * 10 ** 18)\n\"\"\"\"\"\"\n## Write code using thirdweb SDK to mint a new NFT to my own address on the polygon mainnet. make a fastapi wrapper to take nft module key as input and return 'success' upon minting\n# \nfrom nftlabs import NftlabsSdk, SdkOptions\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\napp = FastAPI()\nclass Item(BaseModel):\n  module_key: str\n\n@app.post(\"/mint\")\ndef mint(item: Item):\n    sdk = NftlabsSdk(SdkOptions(), \"https://polygon-rpc.com\")\n    sdk.set_private_key(\"your private key here\")\n    nft_module = sdk.get_nft_module(item.module_key)\n    print(nft_module.mint(MintArg(name=\"name\", description=\"desc\",image_uri=\"add url\", properties={}))\n    return 'success'\n\"\"\"\"\"\"\n## Write code using the thirdweb SDK to accept input of an address, then mint a new NFT to that address. also mint 7 coins of my currency and transfer 5 to a different address. make fastapi wrapper to accept module keys, sender/receiver address and NFT name.\n#\nfrom nftlabs import NftlabsSdk, SdkOptions, MintArg\nfrom fastapi import FastAPI\nfrom pydantic import BaseModel\napp = FastAPI()\nclass Item(BaseModel):\n  nft_module_key: str\n  receiver: str\n  sender: str\n  name: str\n  currency_module_key: str\n@app.post(\"/mint\")\ndef mint(item: Item):\n    sdk = NftlabsSdk(SdkOptions(), \"https://polygon-rpc.com\")\n    sdk.set_private_key(\"your private key here\")\n    nft_module = sdk.get_nft_module(item.nft_module_key)\n    print(nft_module.mint(MintArg(name=item.name, description=\"desc\",image_uri=\"add url\", properties={}), \"receivers address\"))\n    currency_module = sdk.get_currency_module(item.currency_module_key)\n    currency_module.mint(7 * 10 ** 18)\n    currency_module.transfer_from(item.sender, item.receiver, 5 * 10 ** 18)\n    return 'success'\n\"\"\"\"\"\"\n## "+query+"\n#",
    temperature=0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\"\"\"\"\"\""])
    code = response["choices"][0]["text"]
    st.code(code, language="python")
