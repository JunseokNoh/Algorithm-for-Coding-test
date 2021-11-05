//
//  Tree.swift
//  codingTest
//
//  Created by junseok on 2021/11/05.
//

import Foundation


class Node{
    var left:Node!
    var data:Int
    var right:Node!
    
    init(_ data:Int){
        self.data = data
    }
}

func insert_data(_ data:Int, _ head:inout Node!){
    var temp = head
    
    if head == nil{
        head = Node(data)
        return
    }
    
    while temp != nil{
        if temp!.data < data {
            if temp!.right == nil{
                temp!.right = Node(data)
                break
            }else{
                temp = temp!.right
            }
        }else{
            if temp!.left == nil{
                temp!.left = Node(data)
                break
            }else{
                temp = temp!.left
            }
        }
    }
}

func preorder_travel(_ node: Node!){
    if node == nil{
        return
    }
    
    print(node.data)
    preorder_travel(node.left)
    preorder_travel(node.right)
}

//var head:Node! = nil
//
//insert_data(5, &head)
//insert_data(4, &head)
//insert_data(6, &head)
//insert_data(7, &head)
//insert_data(10, &head)
//insert_data(1, &head)
//insert_data(2, &head)
//
//
//print(head.data)
//
//preorder_travel(head)
