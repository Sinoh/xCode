//
//  HomeCell.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/28/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class HomeView: BaseCell, UICollectionViewDataSource {

// Constants
//==============================================================================================================================================================================================================================================
  
    let cellId = "cellId"
    
    
// Variables
//==============================================================================================================================================================================================================================================
    
    var homeController: HomeController?
    
    var icons: [Icon] = {
        var restaurants = Icon(name: "Restaurants", imageName: "restaurant")
        var drinks = Icon(name: "Drinks", imageName: "boba")
        var salon = Icon(name: "Salon", imageName: "hair")
        var spa = Icon(name: "Relax", imageName: "massage")
        var travel = Icon(name: "Travel", imageName: "travel")
        var shopping = Icon(name: "Shopping", imageName: "shopping-cart")
        var sport = Icon(name: "Activity", imageName: "heartbeat")
        var event = Icon(name: "Events", imageName: "calendar")
        var forum = Icon(name: "Forum", imageName: "speech-bubble")
        
        return [restaurants, drinks, salon, spa, travel, shopping, sport, event, forum]
    }()
    
    lazy var collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.backgroundColor = UIColor.white
        cv.dataSource = self
        cv.delegate = self
        return cv
    }()
    

// Functions
//==============================================================================================================================================================================================================================================
    override func setupViews() {
        super.setupViews()
        
        backgroundColor = .blue
        
        // Makes the collection view, the icons, shift down 80, 55 to the right
        collectionView.contentInset = UIEdgeInsetsMake(80,0,0,55)
        addSubview(collectionView)
        
        addConstraintsWithFormat(format: "H:|[v0]|", views: collectionView)
        addConstraintsWithFormat(format: "V:|[v0]|", views: collectionView)
        
        collectionView.register(IconCell.self, forCellWithReuseIdentifier: cellId)

    }
    
    
     // Creates 5 collection view cells
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
     return icons.count
     }
     
     func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
     let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! IconCell
        
     cell.icon = icons[indexPath.item]
        
     return cell
     }
     
     // Makes the size of the cell
     func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
     return CGSize(width: 90, height: 145)
     }
     
     func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
     return 0
     }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
    
        print(indexPath.item)
        homeController?.showBusinessController()
        
    }
    
    
    
}

protocol MyDelegate: class {
    func onButtonTapped()
}

class MyView: UIView {
    weak var delegate: MyDelegate?
    
    let button = UIButton()
    
    
    button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    
    func buttonTapped() {
        self.delegate?.onButtonTapped()
    }
}













