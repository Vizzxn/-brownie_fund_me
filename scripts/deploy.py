from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


DECIMALS = 18
STARTING_PRICE = 2000

if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    price_feed_address = config("networks")[network.show_active()]["eth_usd_price_feed"]

else:
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": get_account()},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
