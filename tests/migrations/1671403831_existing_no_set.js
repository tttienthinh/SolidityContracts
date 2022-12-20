const ExistingNoSet = artifacts.require("ExistingNoSet")

module.exports = function(_deployer) {
  _deployer.deploy(ExistingNoSet)
};
