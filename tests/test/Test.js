const Test = artifacts.require("./Test")

contract("Test", accounts => {
    it("setFavoriteNumber", async function() {
        const Contract = await Test.deployed();
        const result = await Contract.setFavoriteNumber(47, {from: accounts[0]});
    }) 
    it("Addition par 5", async function() {
        const Contract = await Test.deployed();
        const result = await Contract.addition(47, {from: accounts[0]});
        console.log(result);
        assert.equal(result.words[0], 47 + 5)
    }) 
    it("Multiplication", async function() {
        const Contract = await Test.deployed();
        const result = await Contract.multiplication(3, 4, {from: accounts[0]});
        console.log(result);
        assert.equal(result.words[0], 12)
    }) 
})

const FavoriteNumber = artifacts.require("./FavoriteNumber")

contract("FavoriteNumber", accounts => {
    it("should change the favorite number in the blockchain", async function() {
        const Contract = await FavoriteNumber.deployed();
        const result = await Contract.setFavoriteNumber(47, {from: accounts[0]})
    }) 
    it("should get the favorite number in the blockchain", async function() {
        const Contract = await FavoriteNumber.deployed();
        const number = await Contract.getFavoriteNumber();
        console.log(number)
        assert.equal(number.words[0], 47, "Not equal to 47")
    }) 
})