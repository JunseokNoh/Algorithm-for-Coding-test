//
//  LinkedList.swift
//  codingTest
//
//  Created by junseok on 2021/11/05.
//

import Foundation

class Linkedlist{
    var head:Node!
    
    func insert(_ data:Int){
        if head == nil{
            head = Node(data: data)
            return
        }
        
        var temp = head
        while temp != nil{
            if temp!.next == nil{
                temp?.next = Node(data: data)
                temp = temp!.next
            }
            temp = temp!.next
        }
    }
    
    func printAll(){
        var temp = head
        while temp != nil{
            print(temp!.data)
            temp = temp?.next
        }
    }
    
    func printReverse(_ node:Node!){
        if node == nil{
            return
        }
        
        printReverse(node.next)
        print(node.data)
    }
    
    class Node{
        var data:Int
        var next:Node!
        
        init(data:Int){
            self.data = data
        }
    }
}

//var linked_list = Linkedlist()
//linked_list.insert(1)
//linked_list.insert(2)
//linked_list.insert(3)
//linked_list.insert(4)
//linked_list.insert(5)
//linked_list.insert(6)
//linked_list.insert(7)
//
//linked_list.printAll()
//linked_list.printReverse(linked_list.head)
