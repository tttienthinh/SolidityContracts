const ExistingFavoriteNumber = artifacts.require("./ExistingFavoriteNumber");
const FavoriteNumber = artifacts.require('./FavoriteNumber');
let address = "";

contract("FavoriteNumber", accounts => {
    it("Get Address", async function () {
        const Contract = await FavoriteNumber.deployed();
        address = Contract.contract._address;
        console.log(address);
    })
    it("should change the favorite number in the blockchain", async function() {
        const Contract = await FavoriteNumber.deployed();
        const result = await Contract.setFavoriteNumber(47, {from: accounts[0]})
    }) 
    it("should get the favorite number in the blockchain", async function() {
        const Contract = await FavoriteNumber.deployed();
        const number = await Contract.getFavoriteNumber();
        console.log(number);
        assert.equal(number.words[0], 47, "Not equal to 47");
    }) 
})

contract("ExistingFavoriteNumber", accounts => {
    it("Set address account", async function() {
        const Contract = await ExistingFavoriteNumber.deployed();
        const result = await Contract.existing(address, {from: accounts[0]});
        console.log(address);
    })
    it("Get", async function() {
        const Contract = await ExistingFavoriteNumber.deployed();
        const result = await Contract.getA({from: accounts[0]});
        console.log(result);
    })
    it("Set", async function() {
        const Contract = await ExistingFavoriteNumber.deployed();
        const result = await Contract.setA(42, {from: accounts[0]});
    })
    it("Get", async function() {
        const Contract = await ExistingFavoriteNumber.deployed();
        const result = await Contract.getA({from: accounts[0]});
        console.log(result);
    })

})