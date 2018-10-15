//
//  SearchView.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/29/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit
import GoogleMaps

class SearchView: BaseCell, UICollectionViewDataSource {
    
    // Constants
    //==============================================================================================================================================================================================================================================
    let searchId = "searchId"
    
    
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

        addSubview(collectionView)
        
        addConstraintsWithFormat(format: "H:|[v0]|", views: collectionView)
        addConstraintsWithFormat(format: "V:|[v0]|", views: collectionView)
        
        collectionView.register(SearchCell.self, forCellWithReuseIdentifier: searchId)
    }
    
    
    // Creates 5 collection view cells
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: searchId, for: indexPath) as! SearchCell
        cell.searchCellDetail?.viewDidLoad()
        return cell
    }
    
    // Makes the size of the cell
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: frame.width, height: frame.height)
    }
    
}
