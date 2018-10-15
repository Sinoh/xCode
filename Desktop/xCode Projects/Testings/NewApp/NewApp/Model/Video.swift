//
//  Video.swift
//  NewApp
//
//  Created by Jeffery Ho on 7/17/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class Video: NSObject {
    
    var thumbnailImageName: String?  // String? means optional string
    var title: String?
    var numberOfViews: NSNumber?
    var uploadDate: NSDate?
    
    var channel: Channel?
    
}

class Channel: NSObject {
    var name: String?
    var profileImageName: String?
}

