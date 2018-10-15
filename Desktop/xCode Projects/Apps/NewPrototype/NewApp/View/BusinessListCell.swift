//
//  BusinessListCell.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/29/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class BusinessListCell: BaseCell {
    
    var business: Business? {
        didSet {
            nameLabel.text = business?.businessName
            locationLabel.text = business?.location
            phoneLabel.text = business?.phone
            websiteLabel.text = business?.website
            detailsLabel.text = business?.details
            distanceLabel.text = "10 mi"
            hoursLabel.text = business?.hours
            priceLabel.text = business?.prices
            
            
            if let imageName = business?.logo {
                iconImageView.image = UIImage(named: imageName)?.withRenderingMode(.alwaysTemplate)
            }
        }
    }
    
    var nameLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 15)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        //label.backgroundColor = UIColor.blue
        return label
    }()
    
    var locationLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 15)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        //label.backgroundColor = UIColor.red
        return label
    }()
    
    var phoneLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 15)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        //label.backgroundColor = UIColor.green
        return label
    }()
    
    var websiteLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 15)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        //label.backgroundColor = UIColor.yellow
        return label
    }()
    
    var detailsLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 30)
        //label.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)
        //label.backgroundColor = UIColor.gray
        return label
    }()
    
    var distanceLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.backgroundColor = UIColor.purple
        label.textColor = .lightGray
        return label
    }()
    
    var hoursLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.backgroundColor = UIColor.brown
        label.textColor = .lightGray
        return label
    }()
    
    var priceLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.italicSystemFont(ofSize: 11)
        //label.backgroundColor = UIColor.cyan
        label.textColor = .lightGray
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
        addSubview(distanceLabel)
        addSubview(hoursLabel)
        addSubview(priceLabel)
        
        addConstraintsWithFormat(format: "H:|-10-[v1(130)]-7-[v0]-60-|", views: nameLabel, iconImageView)
        addConstraintsWithFormat(format: "H:|-147-[v0]-60-|", views: locationLabel)
        addConstraintsWithFormat(format: "H:|-147-[v0]-60-|", views: phoneLabel)
        addConstraintsWithFormat(format: "H:|-147-[v0]-60-|", views: websiteLabel)
        addConstraintsWithFormat(format: "H:|-10-[v0]-10-|", views: detailsLabel)
        addConstraintsWithFormat(format: "H:|-[v0(60)]-10-|", views: distanceLabel)
        addConstraintsWithFormat(format: "H:|-[v0(60)]-10-|", views: hoursLabel)
        addConstraintsWithFormat(format: "H:|-[v0(60)]-10-|", views: priceLabel)
        
        
        addConstraintsWithFormat(format: "V:|-10-[v0(20)]-5-[v1(20)]-5-[v2(20)]-5-[v3(20)]-5-[v4]-10-|", views: nameLabel, locationLabel, phoneLabel, websiteLabel, detailsLabel)
        addConstraintsWithFormat(format: "V:|-10-[v0(20)]-0-[v1(20)]-0-[v2(20)]", views: distanceLabel, hoursLabel, priceLabel)
        
        addConstraintsWithFormat(format: "H:|[v0]|", views: separatorView)
        addConstraintsWithFormat(format: "V:[v0(1)]|", views: separatorView)
        addConstraint(NSLayoutConstraint(item: iconImageView, attribute: .top, relatedBy: .equal, toItem: nameLabel, attribute: .top, multiplier: 1, constant: 0))
        addConstraint(NSLayoutConstraint(item: iconImageView, attribute: .bottom, relatedBy: .equal, toItem: websiteLabel, attribute: .bottom, multiplier: 1, constant: 0))
        
    }
}
