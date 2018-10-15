//
//  VideoCell.swift
//  NewApp
//
//  Created by Jeffery Ho on 7/16/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class BaseCell: UICollectionViewCell {
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
    
    
class VideoCell: BaseCell {
    
    var video: Video? {
        didSet {
            titleLabel.text = video?.title
            thumbnailImageView.image = UIImage(named: (video?.thumbnailImageName)!)
            
            // Safe way to call
            if let profileImageName = video?.channel?.profileImageName {
                userProfileImageView.image = UIImage(named: profileImageName)
                
            }
            
            if let channelName = video?.channel?.name, let numberOfViews = video?.numberOfViews {
                
                let numberFormatter = NumberFormatter()
                numberFormatter.numberStyle = .decimal // groups numbers with commas
                
                let subtitleText = "\(channelName) • \(numberFormatter.string(from: numberOfViews)!) • 2 years ago "  // How the string of the subtitle text is written
                subtitleTextView.text = subtitleText
            }
            
            // measure title text
            if let title = video?.title {
                let size = CGSize(width: frame.width - 16 - 44 - 8 - 16, height: 1000)
                let options = NSStringDrawingOptions.usesFontLeading.union(.usesLineFragmentOrigin)
                let estimatedRect = NSString(string: title).boundingRect(with: size, options: options, attributes: [kCTFontAttributeName as NSAttributedStringKey: UIFont.systemFont(ofSize: 14)], context: nil)
                
                
                if estimatedRect.size.height > 20 {
                    titleLabelHeightConstraint?.constant = 44
                }
                else {
                    titleLabelHeightConstraint?.constant = 20
                }
            }
        }
    }
    
    // Makes the thumbnail cell blue and stops Autosizing
    // translatesAutoresizingMaskIntoConstraints is set false within addConstraints
    let thumbnailImageView: UIImageView = {
        let imageView = UIImageView()
        //        imageView.backgroundColor = UIColor.blue                          // With the thumbnail set to a pic, this line is not needed
        //        imageView.translatesAutoresizingMaskIntoConstraints = false
        imageView.image = UIImage(named: "BlankSpace")                      // Sets thumbnail to a image named "BlankSpace"
        imageView.contentMode = .scaleAspectFill                            // Changes the aspect ratio of the image to the original
        imageView.clipsToBounds = true                                      // Clip the image
        return imageView
    }()
    
    //Makes the user profile imageview
    let userProfileImageView: UIImageView = {
        let imageView = UIImageView()
        //        imageView.backgroundColor = UIColor.green                         // With the profile image set to a pic, this line is not needed
        imageView.image = UIImage(named: "TaylorSwift")                     // Sets the profile image to "TaylorSwift"
        imageView.layer.cornerRadius = 22                                   // Sets corner radius of the proifle image to 22, shoulf be half of the profile imageview size
        imageView.layer.masksToBounds = true                                // Sets masking to true
        return imageView
    }()
    
    // Makes a black line for a separator
    // translatesAutoresizingMaskIntoConstraints is set false within addConstraints
    let separatorView: UIView = {
        let view = UIView()
        //        view.backgroundColor = UIColor.black                                                                  // Not needed anytmore after the line following this one
        view.backgroundColor = UIColor(displayP3Red: 230/255, green: 230/255, blue: 230/55, alpha: 1)           // A more accurate color than just back
        //view.translatesAutoresizingMaskIntoConstraints = false
        return view
    }()
    
    let titleLabel: UILabel = {
        let label = UILabel()
        //       label.backgroundColor = UIColor.purple                             // This line is not neededd as it is the background color for the text
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Taylor Swift - Blank Space"                           // Sets the text in the title lable
        label.numberOfLines = 2
        return label
    }()
    
    let subtitleTextView: UITextView = {
        let textView = UITextView()
        //        textView.backgroundColor = UIColor.red                            // This line is not needed as it is the background color for the text
        textView.translatesAutoresizingMaskIntoConstraints = false
        textView.text = "TaylorSwiftVEVO • 1,604,684,607 views • 2 years ago"   // Sets the text in the subtitle lable
        textView.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)         // Offsets text position to be 4 pixels higher than the orgin
        textView.textColor = UIColor.lightGray
        return textView
    }()
    
    var titleLabelHeightConstraint: NSLayoutConstraint?
    
    // Creates constraints for thumbnail and separator
    override func setupViews() {
        addSubview(thumbnailImageView)
        addSubview(separatorView)
        addSubview(userProfileImageView)
        addSubview(titleLabel)
        addSubview(subtitleTextView)
        
        
        // Manually add each constraint to each cell
        //addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "H:|-16-[v0]-16-|", options: NSLayoutFormatOptions(), metrics: nil, views: ["v0": thumbnailImageView]))
        // Added vertical constraint to both thumbnail and separator
        //addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "V:|-16-[v0]-16-[v1(1)]|", options: NSLayoutFormatOptions(), metrics: nil, views: ["v0": thumbnailImageView, "v1": separatorView]))
        
        // Add horizontal constraints to the separator
        //addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "H:|[v0]|", options: NSLayoutFormatOptions(), metrics: nil, views: ["v0": separatorView]))
        // Vertial constrait already added to separator through "[v1(1)]"
        //addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "V:[v0(1)]|", options: NSLayoutFormatOptions(), metrics: nil, views: ["v0": separatorView]))
        
        
        
        // Add horizontal constraints to the thumbnail. 16 pixels from the left, 16 pixels from the right
        addConstraintsWithFormat(format: "H:|-16-[v0]-16-|", views: thumbnailImageView)
        
        // Add veritcal constraints to the thumbnail and separator. 16 pixels from the top, 16 pixels from the bottom
        //addConstraintsWithFormat(format: "V:|-16-[v0]-16-[v1(1)]|", views: thumbnailImageView, separatorView)
        
        // Add horizontal constraints to the userprofile image and constraint it to 44 pixels wide. 16 pixels from the left and 44 pixels from that point
        addConstraintsWithFormat(format: "H:|-16-[v0(44)]", views: userProfileImageView)
        
        // Add vertical constraints to the thumbnail, userprofile separartor. 16 pixels from the top, then to the bottom of the thumbnail. 8 pixels between the thumbnail and user profile then the user profile is from that point until 44 pixels down. Then 16 pixles from the separator which is 1 pixel tall.
        addConstraintsWithFormat(format: "V:|-16-[v0]-8-[v1(44)]-36-[v2(1)]|", views: thumbnailImageView, userProfileImageView, separatorView)
        
        // Add horizontal constraints to the separator
        addConstraintsWithFormat(format: "H:|[v0]|", views: separatorView)
        
        
        
        // Top Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .top, relatedBy: .equal, toItem: thumbnailImageView, attribute: .bottom, multiplier: 1, constant: 8))
        
        // Left Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .left, relatedBy: .equal, toItem: userProfileImageView, attribute: .right, multiplier: 1, constant: 8))
        
        // Right Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .right, relatedBy: .equal, toItem: thumbnailImageView, attribute: .right, multiplier: 1, constant: 0))
        
        // Height Constraint for Title Label
        titleLabelHeightConstraint = NSLayoutConstraint(item: titleLabel, attribute: .height, relatedBy: .equal, toItem: self, attribute: .height, multiplier: 0, constant: 44)
        addConstraint(titleLabelHeightConstraint!)
        
        // Top Constraint for Subtitle
        addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .top, relatedBy: .equal, toItem: titleLabel, attribute: .bottom, multiplier: 1, constant: 4))
        
        // Left Constraint for Subtitle
        addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .left, relatedBy: .equal, toItem: userProfileImageView, attribute: .right, multiplier: 1, constant: 8))
        
        // Right Constraint for Subtitle
        addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .right, relatedBy: .equal, toItem: thumbnailImageView, attribute: .right, multiplier: 1, constant: 0))
        
        // Height Constraint for Subtitle
        addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .height, relatedBy: .equal, toItem: self, attribute: .height, multiplier: 0, constant: 30))
        
    }
    
}
