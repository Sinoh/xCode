//
//  AccountCell.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/29/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class AccountCell: BaseCell {
    
    var account: Account? {
        didSet {
            nameLabel.text = account?.name
        }
    }
    
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.backgroundColor = .white
        label.font = UIFont.systemFont(ofSize: 13)
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
    
    let profilePicture: UIImageView = {
        let imageView = UIImageView()
        imageView.backgroundColor = .blue
        imageView.contentMode = .scaleAspectFill
        return imageView
    }()
 
    
    override func setupViews() {
        super.setupViews()
        
        addSubview(nameLabel)
        addSubview(iconImageView)
        addSubview(separatorView)
        
        addConstraintsWithFormat(format: "H:|-20-[v1(30)]-8-[v0]|", views: nameLabel, iconImageView)
        addConstraintsWithFormat(format: "V:|[v0]|", views: nameLabel)
        
        addConstraintsWithFormat(format: "H:|[v0]|", views: separatorView)
        addConstraintsWithFormat(format: "V:[v0(1)]|", views: separatorView)
        addConstraintsWithFormat(format: "V:[v0(30)]",  views: iconImageView)
        
        addConstraint(NSLayoutConstraint(item: iconImageView, attribute: .centerY, relatedBy: .equal, toItem: self, attribute: .centerY, multiplier: 1, constant: 0))
    }
}

