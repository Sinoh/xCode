//
//  ViewController.swift
//  NewApp
//
//  Created by Jeffery Ho on 7/14/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class HomeController: UICollectionViewController, UICollectionViewDelegateFlowLayout {
    
    

    // Create Video om video in an array
    var videos: [Video] = {
        var kanyeChannel = Channel()
        kanyeChannel.name = "KanyeIsTheBestChannel"
        kanyeChannel.profileImageName = "kanye_profile"
        
        var blankSpaceVideo = Video()
        blankSpaceVideo.title = "Taylor Swift - Blank Space"
        blankSpaceVideo.thumbnailImageName = "BlankSpace"
        blankSpaceVideo.channel = kanyeChannel
        blankSpaceVideo.numberOfViews = 1231452433
        
        var badBloodVideo = Video()
        badBloodVideo.title = "Taylor Swift - Bad Blood featuring Kendrick Lamar"
        badBloodVideo.thumbnailImageName = "taylor_swift_bad_blood"
        badBloodVideo.channel = kanyeChannel
        badBloodVideo.numberOfViews  = 1249372492
        
        return [blankSpaceVideo, badBloodVideo]
    }()
/*
    func fetchVideos() {
        let url = NSURL(string: "https://s3-us-west-2.amazonaws.com/youtubeassets/home.json")
        NSURLSession.sharedSession().dataTaskWithURL(url!) { (data, response, error) in
            
            if error != nil {
                print(error)
                return
            }
            
            let str = NSString(data: data!, encoding: NSUTF8StringEncoding)
            print(str)
            
        }.resume
    }
*/
    override func viewDidLoad() {
        super.viewDidLoad()

        navigationItem.title = "Home"
        navigationController?.navigationBar.isTranslucent = false                       // Makes the navigation bar translucent
        
        
        let titleLabel = UILabel(frame: CGRect(x: 0, y: 0, width: view.frame.width - 32, height: view.frame.height))  // Initialize the title Labe, wdith - 32 just happens to be good. Test different numbers
//        let titleLabel = UILabel(frame: CGRectMake(0, 0, view.frame.width - 32, view.frame.height))
        titleLabel.text = "Home"
        titleLabel.textColor = UIColor.white                                            // Set the text color to white                                    // Sets the font size to 20
        titleLabel.font = UIFont(name: "Home", size: 20.0)                              // Sets the font size
        navigationItem.titleView = titleLabel
        
        collectionView?.backgroundColor = UIColor.white
        collectionView?.register(VideoCell.self, forCellWithReuseIdentifier: "cellId")
        
        // Makes the collection view, the videos, shift down 50, so its not under the navigation bar
        collectionView?.contentInset = UIEdgeInsetsMake(50, 0, 0, 0)
        
        // Makes the scroll 50 pixels lower so it doesn't go under the navigation bar
        collectionView?.scrollIndicatorInsets = UIEdgeInsetsMake(50, 0, 0, 0)
        
        setupMenuBar()
        setupNavBarButtons()
    }
    
    // Adds functional navigation buttons to the navigation bar
    func setupNavBarButtons() {
        let searchImage = UIImage(named: "search_icon")?.withRenderingMode(.alwaysOriginal)
        let searchBarbuttonItem = UIBarButtonItem(image: searchImage, style: .plain, target: self, action: #selector(handleSearch))
        
        let moreButton = UIBarButtonItem(image: UIImage(named: "nav_more_icon")?.withRenderingMode(.alwaysOriginal), style: .plain, target: self, action: #selector(handleMore))
        
        navigationItem.rightBarButtonItems = [moreButton, searchBarbuttonItem]
    }
    
    // This function is called when the more button is pressed
    @objc func handleMore() {
        
    }
    
    // This function is called when the search button is pressed
    @objc func handleSearch() {
        print(123)
    }
    
    let menuBar: MenuBar = {
        let mb = MenuBar()
        return mb
    }()
    
    private func setupMenuBar() {
        view.addSubview(menuBar)
        view.addConstraintsWithFormat(format: "H:|[v0]|", views: menuBar)
        view.addConstraintsWithFormat(format: "V:|[v0(50)]", views: menuBar)
        
    }
    
    
    // Creates 5 collection view cells
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return videos.count // Displays the number of cells equal to the videos in the array
        
    }
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cellId", for: indexPath) as! VideoCell // as! is downcasting
        
        cell.video = videos[indexPath.item] // Itterates through the array for each video
        
        return cell
    }
    
    // Makes the size of the sell the frame width and a height of 200
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        let height = (view.frame.width - 16 - 16) * 9 / 16                  // Subtract 16 from left side and right side then multiple by 9 by 16 ratio
        return CGSize(width: view.frame.width, height: height + 16 + 94)    // 16 and 68 Calculated from the thumbnail constriants
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 0
    }
    
}


//========================================================================================================================================================================================================================================


//Moved to another group, "View", good practice to split classes up by file
/*
class VideoCell: UICollectionViewCell {
    override init(frame: CGRect) {
        super.init(frame:frame)
        setupViews()
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
    
    let titleLabel: UIView = {
        let label = UILabel()
//       label.backgroundColor = UIColor.purple                             // This line is not neededd as it is the background color for the text
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "Taylor Swift - Blank Space"                           // Sets the text in the title lable
        return label
    }()
   
    let subtitleTextView: UITextView = {
        let textView = UITextView()
//        textView.backgroundColor = UIColor.red                            // This line is not neededd as it is the background color for the text
        textView.translatesAutoresizingMaskIntoConstraints = false
        textView.text = "TaylorSwiftVEVO • 1,604,684,607 views • 2 years ago"   // Sets the text in the subtitle lable
        textView.textContainerInset = UIEdgeInsetsMake(0, -4, 0, 0)         // Offsets text position to be 4 pixels higher than the orgin
        textView.textColor = UIColor.lightGray
        return textView
    }()
    
    // Creates constraints for thumbnail and separator
    func setupViews() {
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
        addConstraintsWithFormat(format: "V:|-16-[v0]-8-[v1(44)]-16-[v2(1)]|", views: thumbnailImageView, userProfileImageView, separatorView)
        
    // Add horizontal constraints to the separator
        addConstraintsWithFormat(format: "H:|[v0]|", views: separatorView)
        
        
        
    // Top Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .top, relatedBy: .equal, toItem: thumbnailImageView, attribute: .bottom, multiplier: 1, constant: 8))
    
    // Left Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .left, relatedBy: .equal, toItem: userProfileImageView, attribute: .right, multiplier: 1, constant: 8))
    
    // Right Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .right, relatedBy: .equal, toItem: thumbnailImageView, attribute: .right, multiplier: 1, constant: 0))
        
    // Height Constraint for Title Label
        addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .height, relatedBy: .equal, toItem: self, attribute: .height, multiplier: 0, constant: 20))

    // Top Constraint for Subtitle
    addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .top, relatedBy: .equal, toItem: titleLabel, attribute: .bottom, multiplier: 1, constant: 4))
    
    // Left Constraint for Subtitle
    addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .left, relatedBy: .equal, toItem: userProfileImageView, attribute: .right, multiplier: 1, constant: 8))
    
    // Right Constraint for Subtitle
    addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .right, relatedBy: .equal, toItem: thumbnailImageView, attribute: .right, multiplier: 1, constant: 0))
    
    // Height Constraint for Subtitle
    addConstraint(NSLayoutConstraint(item: subtitleTextView, attribute: .height, relatedBy: .equal, toItem: self, attribute: .height, multiplier: 0, constant: 30))

    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

*/


//========================================================================================================================================================================================================================================

/*
// Array for constraints
extension UIView {
    func addConstraintsWithFormat(format: String, views: UIView...) {
        var viewsDictionary = [String: UIView]()
        for (index, view) in views.enumerated() {
            let key = "v\(index)"
            view.translatesAutoresizingMaskIntoConstraints = false
            viewsDictionary[key] = view
        }
        
        addConstraints(NSLayoutConstraint.constraints(withVisualFormat: format, options: NSLayoutFormatOptions(), metrics: nil, views: viewsDictionary))
    }
}
*/
// Moved to extenstion file





