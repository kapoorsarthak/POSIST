import time                                                 #to take the timestamp
def create_GenesisNode():
    if(ParentNode==NULL and ParentNode->data):              #if no parent and no data in root 
        GenesisNode=Root                                    #make a new root and make that new root GenesisNode 
        GenesisNode->Rootdata                               #put data in GenesisNode
    else:
        return GenesisNode                                  #if there is already a root genesis node return it

def create_childNodes(Node):
    if(Node->left->data or Node->right->data):              #if root left and root right has data so the node already has childs
        return Node->left->data                             #return left child
        return Node->right->data                            #return right child
    else:
        LeftChild->Node->left->data                          #make new left child
        RightChild->Node->right->data                        #make new right child
        if(LeftChild->data + RightChild-data > Node->data): # if data of both the nodes is greater than the parent node this canot be done
            return 0
        else:
            return LeftChild->data                          #if the sum is not greater return both the nodes                 
            return RightChild-data          
            
def create_childNode(Node):                                 
    if(Node->left->data == True):                           #if root of left exist then 
        RightChild->Node->right->data                       #make a new right node 
    if(Node->right->data == True):                          #if root of left exist then
        LeftChild->Node->left->data                         #make a new left node
    else:
        create_childNodes(Node)                             #if both dont exist then make both the two new nodes

def Encrypt(data):                                          
    arr=[]                                                  
    arr=[ord(c) for c in data]                              #convert the ascii data into decimal
    for i in arr:
        arr[i]=arr[i]+1                                     #add 1 to the decimal 
        data=chr(arr[i])                                    #make the decimal back to ascii

def Decrypt(data):
    arr1=[]
    arr1=[ord(c) for c in data]                             #convert the ascii data into decimal
    for i in arr:
        arr[i]=arr[i]-1                                     #subtract 1 to the decimal
        data=chr(arr[i])                                    #make the decimal back to ascii

class verify:
    def compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId):
        timestamp = time.time()
        str data =Node->data
        int nodeNumber
        str nodeId= Node
        str referenceNodeid = &ParentNode
        str childReferenceNodeId= &children
        str genesisReferenceNodeId= &GenesisNode

    def verify_owner(data, compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId)):
        str a
        a=Decrypt(data)
        if(a==Encrypt(data)):
            new=compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId)
            old=verify.compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId)
            if(new==old):
                verify_owner=True
                
def Transfer_ownership(Decrypt(data), compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId))
        str a
        a=Decrypt(data)
        if(a==Encrypt(data)):
            new=compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId)
            old=verify.compute_hash(timestamp, data, nodeNumber , nodeid, referenceNodeid, childReferenceNodeId, genesisReferenceNodeId)
            if(new==old):
                verify_owner=True
        else:
            return 0
        Transfer_ownership==True
        
def merge_nodes(node1-> data, node2-> data):
    merged data = node1-> data + node2-> data
    
for in in range (x):
    print("How many times the Programme should Run\n")
    x=int(raw_input())
    print("Press 1 for to create Geneis Node\n")
    print("Press 2 for to create create Child Nodes\n")
    print("Press 3 for to create create child Node\n")
    print("Press 4 for to Encrypt\n")
    print("Press 5 for to Decrypt\n")
    print("Press 6 to verify owner\n")
    print("Press 7 to compute hash\n")
    y=int(raw_input())
