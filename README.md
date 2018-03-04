# PyChain

## Summary
now dev in ver 2.0  
Implement blockchain with python.  

### HTTP Method
/mine - GET  
- argument
    - node_identifier : miner account id  
- discription : mining block

/chain - GET
- argument
    - No Argument
- description : get full chain  

/id/apply - POST
- value
    - id(string) : new account id
- description : apply new id

/transactions/new - POST
- value
    - sender(string) : sender id
    - recipient(string) : recipient id
    - amount(int) : amount
- description : making new transactions

/transactions - GET
- argument
    - No Argument
- description : get current transactions

/nodes/register - POST
- values
    - nodes(list) : list of new nodes
- description : add new node

/nodes/resolve - GET
- argument
    - No Argument
- description : resolve consensus



## Notes
- DB application complete
- account system implement successful

## TODO
- Sync feature implement
- Travis Ci and pytest application 

## References
[https://blog.naver.com/pjt3591oo/221181592127](https://blog.naver.com/pjt3591oo/221181592127)
