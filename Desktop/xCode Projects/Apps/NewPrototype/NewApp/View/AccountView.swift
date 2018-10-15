//
//  AccountCell.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/28/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class AccountView: BaseCell, UICollectionViewDataSource {
    
    
// Constants
//==============================================================================================================================================================================================================================================
    let accountId = "accountId"
    let headerId = "headerId"
    
    let headerHeight: CGFloat = 200
    let cellHeight: CGFloat = 50
    
    let accounts: [Account] = {
        return [Account(name: "Profile", iconName: ""), Account(name: "Account Settings", iconName: ""), Account(name: "Posts", iconName: ""), Account(name: "Referrals", iconName: ""), Account(name: "Recent Searches", iconName: ""), Account(name: "Help", iconName: ""), Account(name: "Log In", iconName: ""), Account(name: "Log Out", iconName: "")]
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
        
        collectionView.register(AccountCell.self, forCellWithReuseIdentifier: accountId)
        collectionView.register(AccountCellHeader.self, forCellWithReuseIdentifier: headerId)
        //collectionView.register(UICollectionViewCell.self, forSupplementaryViewOfKind: UICollectionElementKindSectionHeader, withReuseIdentifier: headerId)
    }
    
    /*
    // Initializing the header
    func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, at indexPath: IndexPath) -> UICollectionReusableView {
        let header = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: headerId, for: indexPath)
        header.backgroundColor = .blue
        return header
    }
    // Size of Header
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> CGSize {
        return CGSize(width: frame.width, height: headerHeight)
    }
    */
 
 
    // Creates 5 collection view cells
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return accounts.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        if indexPath.item == 0 {
            let cell = collectionView.dequeueReusableCell(withReuseIdentifier: headerId, for: indexPath) as! AccountCellHeader
            cell.nameLabel.text = "Name: Osaka Sushi"
            cell.locationLabel.text = "Location: Florin Road"
            cell.phoneLabel.text = "Phone: (916) 123-4567"
            cell.websiteLabel.text = "Website: osakasushi.com"
            cell.detailsLabel.text = "Sushi"
            return cell
        }
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: accountId, for: indexPath) as! AccountCell
        cell.account = accounts[indexPath.item]
        return cell
    }
    
    // Makes the size of the cell
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        if indexPath.item == 0 {
            return CGSize(width: frame.width, height: 170)
        }
        return CGSize(width: frame.width, height: 50)
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 0
    }
}

