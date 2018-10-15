//
//  VideoCell.swift
//  NewApp
//
//  Created by Jeffery Ho on 7/16/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class BaseCell: UICollectionViewCell, UICollectionViewDelegate, UICollectionViewDelegateFlowLayout {
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupViews()
    }
        
        func setupViews() {
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
    
    
class IconCell: BaseCell {

    var icon: Icon? {
        didSet {
            titleLabel.text = icon?.thumbnailImageName
            thumbnailImageView.image = UIImage(named: (icon?.thumbnail)!)
            }
        }
    
    // Makes the thumbnail cell blue and stops Autosizing
    // translatesAutoresizingMaskIntoConstraints is set false within addConstraints
    let thumbnailImageView: UIImageView = {
        let imageView = UIImageView()
        imageView.contentMode = .scaleAspectFill                            // Changes the aspect ratio of the image to the original
        imageView.clipsToBounds = true                                      // Clip the image
        return imageView
    }()
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.font = UIFont.systemFont(ofSize: 14.0)
        return label
    }()
    
    var homeController: HomeController?
    
    var titleLabelHeightConstraint: NSLayoutConstraint?
    
    // Creates constraints for thumbnail and separator
    override func setupViews() {
        addSubview(thumbnailImageView)
        addSubview(titleLabel)
        
        // Add horizontal constraints to the thumbnail
        addConstraintsWithFormat(format: "H:|-35-[v0(80)]|", views: thumbnailImageView)
        
        // Add vertical constraints
        addConstraintsWithFormat(format: "V:|-10-[v0(80)]-20-[v1(20)]-30-|", views: thumbnailImageView, titleLabel)

        // Top Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .top, relatedBy: .equal, toItem: thumbnailImageView, attribute: .bottom, multiplier: 1, constant: 0))
        // Left Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .left, relatedBy: .equal, toItem: thumbnailImageView, attribute: .left, multiplier: 1, constant: 0))
        // Right Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .right, relatedBy: .equal, toItem: thumbnailImageView, attribute: .right, multiplier: 1, constant: 0))
        titleLabel.textAlignment = NSTextAlignment.center
        // Height Constraint for Title Label
        titleLabelHeightConstraint = NSLayoutConstraint(item: titleLabel, attribute: .height, relatedBy: .equal, toItem: self, attribute: .height, multiplier: 0, constant: 20)
        addConstraint(titleLabelHeightConstraint!)
    }
 
}

