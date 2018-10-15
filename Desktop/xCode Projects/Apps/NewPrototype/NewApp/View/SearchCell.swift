//
//  SearchCell.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/28/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit
import GoogleMaps

class SearchCell: BaseCell{
    
    var searchCellDetail: SearchCellDetail?
    
    override func setupViews() {
        super.setupViews()
    }
    

}


class SearchCellDetail : UIViewController{
    
    var homeController: HomeController?
    var mapView:GMSMapView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("Hello")
        
        GMSServices.provideAPIKey("AIzaSyCX3Wa8sAXm_NSIZiFMow3UebBDy0xPbpk")
        
        let camera = GMSCameraPosition.camera(withLatitude: -33.86, longitude: 151.20, zoom: 6.0)
        let mapView = GMSMapView.map(withFrame: CGRect(x: 100, y: 100, width: 200, height: 200), camera: camera)
        self.view.addSubview(mapView)
    }
}
