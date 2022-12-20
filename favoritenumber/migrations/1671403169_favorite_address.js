const FavoriteAddress = artifacts.require("FavoriteAddress")

module.exports = function(_deployer) {
  _deployer.deploy(FavoriteAddress)
};
