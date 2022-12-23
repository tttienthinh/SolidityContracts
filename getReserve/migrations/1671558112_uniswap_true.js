const UniswapTrue = artifacts.require("UniswapTrue")

module.exports = function(_deployer) {
  _deployer.deploy(UniswapTrue)
};
