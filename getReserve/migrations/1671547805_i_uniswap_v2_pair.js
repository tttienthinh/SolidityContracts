const IUniswapV2Pair = artifacts.require("IUniswapV2Pair")

module.exports = function(_deployer) {
  _deployer.deploy(IUniswapV2Pair)
};
