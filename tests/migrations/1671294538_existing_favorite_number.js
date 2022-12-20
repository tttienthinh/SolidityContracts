const ExistingFavoriteNumber = artifacts.require("ExistingFavoriteNumber")

module.exports = function(_deployer) {
  _deployer.deploy(ExistingFavoriteNumber)
};
