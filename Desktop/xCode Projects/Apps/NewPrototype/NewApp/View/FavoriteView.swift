//
//  FavoriteView.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/29/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class FavoriteView: BaseCell, UICollectionViewDataSource {
    
    
// Constants
//==============================================================================================================================================================================================================================================
    let favoriteId = "favoriteId"
    
    let headerHeight: CGFloat = 200
    let cellHeight: CGFloat = 50
    
    let businesses: [Business] = {
        return [Business(name: "Osaka Sushi", details: "CODE: Sushi", location: "Florin Road", phone: "(916) 123-4567", logo: "", website: "osakasushi.com", hours: "10am-9pm", prices: "$11"), Business(name: "Osaka Sushi", details: "CODE: Sushi", location: "Florin Road", phone: "(916) 123-4567", logo: "", website: "osakasushi.com", hours: "10am-9pm", prices: "$11")]
    }()
    
// Variables
//==============================================================================================================================================================================================================================================
    
    var homeController: HomeController?
    
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
        addSubview(collectionView)
        
        addConstraintsWithFormat(format: "H:|[v0]|", views: collectionView)
        addConstraintsWithFormat(format: "V:|[v0]|", views: collectionView)
        
        collectionView.register(BusinessListCell.self, forCellWithReuseIdentifier: favoriteId)

    }
    
    
    // Creates 5 collection view cells
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return businesses.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: favoriteId, for: indexPath) as! BusinessListCell
        let business = businesses[indexPath.item]
        cell.business = business
        return cell
        
    }
    
    // Makes the size of the cell
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: frame.width, height: 165)
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 0
    }
}
