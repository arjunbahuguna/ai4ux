1. [Link to demo-video](https://wetransfer.com/downloads/d30e575ed297db77329d92ad95771ced20210307215448/8a2a49)<br>
2. [Link to XD website design](https://xd.adobe.com/view/5789e5de-1b5b-4805-99c5-45a0700862df-02da/?fullscreen)
3. 
## Commentree (Evaluate your UX through actual users!)

### The Problem
UX designers value user feedback highest. The user's word is the gold standard. But we often overlook the greatest source of user feedback: social media. In ignoring the 'collective knowledge' of their user group and by not being able to listen to their UI complaints online, UX designers miss out on important insights.

## The Solution
Using machine learning for social media analysis, we mine existing user feedback (user reviews, tweets, etc) about a product available on social media sites like Twitter, Facebook, Instagram to recommend UX/UI design changes. This gives the UX designer continuous and direct feedback from their actual users, and our analysis recommends changes to the design.

## The Framework
We use the below framework to measure our product's UX from online reviews posted to social media.
<img src="https://raw.githubusercontent.com/standard-deviant/ai4ux/main/hexagon.jpeg">


## Process (UML diagram - flow of data across system)
## The Data
The users' feedback has been sourced from Twitter & App store reviews for this prototype, but can be sourced from any social media or app platform we want. The text data from the tweets contain words that can trigger one of the seven prongs of our UX framework. By mapping the text data of the tweet to our framework, we can evaluate the UX of the product.

## The Analysis
We use multiple analysis techniques from natural language processing (NLP) and supervised machine learning to do analysis on user tweets. Some of these techniques include:
### 1. Sentiment analysis: Gain a measure of user satisfaction from the tweet by algorithmically measuring how positive or negative the sentiment of the tweet is.
### 2. 
### 3. 
### 4. 

## The Insights

## Impact to Society of Solution:
| Problems in rural microfinance | How our project solves them |
| --- | --- |
| Predatory loans from banks, moneylenders | Zero interest microloans |
| Patchy maintenance of accounts | Automatic maintenance of fault-tolerant, decentralized ledger |
| Certain groups (women, dalits) not allowed into groups | Anonymity on the network ensures equality for all|
| Need for centralized organisational leadership | Auto-governance by solidity smart contract |                                         | Risk of non-repayment of loans is high | Risk is mitigated by introducing peer-pressure on the blockchain (main innovation) |
| Possibility of corruption inside group | All transactions are open and transparent |
| [Rural people find bank braches forbidding](https://thewire.in/171614/microfinance-bandhan-public-sector-banks/) | Intuitive single-page web-interface for all transactions |


#### Peer Pressure on the blockchain (main innovation)
Solidarity lending (peer pressure and mutual accountability to repaying loans) is an building block of rural microfinance. But in a pan-India digital network, this peer-pressure would be minimised. We achieve peer-pressure on a peer-to-peer network by using a novel accountability solution, as described below.
A new member on the network can only be added once his Aadhar identity been physically **validated by 4 pre-existing nodes on the network**. If the person defaults, the four people responsibility for him are required to either make him pay or split his debt. This roots the digital network in physical space, and simulates the same social pressure necessary for solidarity lending groups.

### Zero-Interest loans
This is made possible by removing traditional banks from the equation. The group pools money internally and acts as a seed-funding co-operative, every three months.


## Architecture and Tech-stack

![System Architecture](https://raw.githubusercontent.com/jangidkrishna/0xSHG/master/architecture.jpg)


### Architecture Modules
##### 1. Validation
Initial members of the network call add_member to add a new person to the network, once they've validated his identity using Aadhar.
##### 2. Deposit Money
The newly added member must deposit money to the pool to be able to request a loan.
##### 3. Request Loan
A person can request a loan if 
  1. He has been validated by 4 existing members
  2. He has deposited some amount of money
##### 4. Receive Loan
All loan request are sorted in increasing order of loan-request amount. Every three months, the money in pool is used to fullfill the maximum number of loan-requests. Any reserve wealth in the pool is re-distributed back to the network. The is the function of pay_loan.

### Tech Stack
1. Ethereum smart constracts (in solidity)
2. Ropsten testnet  
3. Truffle framework
4. MetaMask
5. Remix IDE
6. Web3.js
7. Aadhar-validator.js


##### Steps to compile in Truffle
1. git clone https://github.com/SatoshiNextTechLab/0xSHG/
2. truffle compile
3. truffle migrate
4. truffle console
5. Interact using Web3.js


##### Steps to compile GUI
1. clone repo https://github.com/SatoshiNextTechLab/0xSHG/
2. cd into 0xSHG-master/GUI
2. npm install .
3. bower install
4. gulp serve

##### Steps to interact and test quickly on Remix with MetaMask
1. go to https://remix.ethereum.org/
2. Ensure MetaMask is setup and connected to Ropsten Network
3. load the SmartContract at https://github.com/SatoshiNextTechLab/0xSHG/blob/master/contracts/driver1.sol
4. Compile the contract, move to tab run.
5. In load contract address enter `0x60a5a1971d1c66D754C6Fbfac17DD1EBe6BAdcef`.Hit At Address button.

### The Team
1. Daksha Dixit
2. Simran Singh
3. Arnav Ajay
4. Arjun Bahuguna
5. Poojita Sure
