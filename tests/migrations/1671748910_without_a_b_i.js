const withoutABI = artifacts.require("withoutABI")

module.exports = function(_deployer) {
  _deployer.deploy(withoutABI)
};
