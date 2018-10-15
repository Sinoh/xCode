//
//  AccountCellHeader.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/29/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//
import UIKit

class AccountCellHeader: BaseCell {
    
    var account: Account? {
        didSet {
            nameLabel.text = account?.name
        }
    }
    
    
    var nameLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        return label
    }()
    
    var locationLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        return label
    }()
    
    var phoneLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        return label
    }()
    
    var websiteLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        return label
    }()
    
    var detailsLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        return label
    }()
    
    let separatorView: UIView = {
        let view = UIView()
        view.backgroundColor = .lightGray
        view.translatesAutoresizingMaskIntoConstraints = false
        return view
    }()
    
    let iconImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.backgroundColor = .blue
        imageView.contentMode = .scaleAspectFill
        return imageView
    }()

    
    override func setupViews() {
        super.setupViews()
        
        addSubview(nameLabel)
        addSubview(locationLabel)
        addSubview(phoneLabel)
        addSubview(websiteLabel)
        addSubview(detailsLabel)
        addSubview(iconImageView)
        addSubview(separatorView)
        
        addConstraintsWithFormat(format: "H:|-20-[v1(100)]-10-[v0]-10-|", views: nameLabel, iconImageView)
        addConstraintsWithFormat(format: "H:|-130-[v0]-10-|", views: locationLabel)
        addConstraintsWithFormat(format: "H:|-130-[v0]-10-|", views: phoneLabel)
        addConstraintsWithFormat(format: "H:|-130-[v0]-10-|", views: websiteLabel)
        addConstraintsWithFormat(format: "H:|-20-[v0]-10-|", views: detailsLabel)

        addConstraintsWithFormat(format: "V:|-15-[v0(20)]-6-[v1(20)]-6-[v2(20)]-6-[v3(20)]-6-[v4(40)]-|", views: nameLabel, locationLabel, phoneLabel, websiteLabel, detailsLabel)
        
        addConstraintsWithFormat(format: "V:[v0(100)]",  views: iconImageView)
        addConstraintsWithFormat(format: "H:|[v0]|", views: separatorView)
        addConstraintsWithFormat(format: "V:[v0(1)]|", views: separatorView)
        addConstraint(NSLayoutConstraint(item: iconImageView, attribute: .top, relatedBy: .equal, toItem: nameLabel, attribute: .top, multiplier: 1, constant: 0))
    }
}


