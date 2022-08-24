//
//  ViewController.swift
//  uploadImage
//
//  Created by 篠原優仁 on 2022/05/21.
//

import UIKit
import Firebase
import FirebaseStorageUI
import FirebaseAuth
import CropViewController


class ViewController: UIViewController,UINavigationControllerDelegate,UIImagePickerControllerDelegate,CropViewControllerDelegate{
    
    
    var count = 0

    
    @IBOutlet weak var imageViewpicker: UIImageView!
    
    @IBOutlet weak var testLabel: UILabel!
    
    
    //アラートを表示させる + Pythonで作成したAPIを叩くためのプログラム
    @IBAction func uploadImageButton(){
     //   print("アップロードされました")
        uploadImage()
        print("tapped")
        

        count += 1
        UserDefaults.standard.set(count, forKey: "count")
//        let getcount = UserDefaults.standard.integer(forKey: "count")
        //UserDefaults.standard.set(count, forKey: "count")
        count = UserDefaults.standard.object(forKey: "count") as! Int

        print(count)
        let alert = UIAlertController(title: "カレンダーに予定を送ります。", message: "count:\(count)", preferredStyle: .alert)
        let action = UIAlertAction(title: "OK", style: .default, handler: nil)
        alert.addAction(action)
        present(alert,animated: true,completion: nil)
    }
    
    @IBAction func imagecropping(_ sender: Any) {
        setImagePicker()
    }
    
    @IBAction func camerabutton(_ sender: Any) {
        let imagePickerController = UIImagePickerController()
        imagePickerController.sourceType = .camera
        imagePickerController.delegate = self
        present(imagePickerController,animated: true,completion: nil)
    }
    
    @IBOutlet weak var uplaodimagebutton2: UIButton!
    
    @IBOutlet var imagecroppingoutlet: UIView!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        uplaodimagebutton2.layer.cornerRadius = 5.0
        imagecroppingoutlet.layer.cornerRadius = 5.0
    }
    
    func uploadImage(){
        
        let storageref = Storage.storage().reference(forURL: "gs://loadimage-9bac0.appspot.com/").child("post\(count)")
        
        let image = imageViewpicker.image!
//        "hoge.jpeg"
        
        let data = image.jpegData(compressionQuality: 1.0)! as NSData
        //              !
        storageref.putData(data as Data, metadata: nil) { (data, error) in
            if error != nil {
                return
            }
            self.dismiss(animated: true, completion: nil)
        }
        
        
    }
    
    func loadImage(){
        let storageref = Storage.storage().reference(forURL: "gs://loadimage-9bac0.appspot.com/").child("post")
        
        imageViewpicker.sd_setImage(with: storageref)
    }
    
    
    func imagePickerController2(_ picker:UIImagePickerController,didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]){
        imageViewpicker.image = info[UIImagePickerController.InfoKey.originalImage] as? UIImage
        dismiss(animated: true, completion: nil)
    }
    
    func setImagePicker(){
            let picker = UIImagePickerController()
            picker.sourceType = .camera
            picker.delegate = self
            present(picker, animated: true, completion: nil)
            
        }
    
    func cropViewController(_ cropViewController: CropViewController, didCropToImage image: UIImage, withRect cropRect: CGRect, angle: Int) {
           updateImageViewWithImage(image, fromCropViewController: cropViewController)
       }
           
       func updateImageViewWithImage(_ image: UIImage, fromCropViewController cropViewController: CropViewController) {
           imageViewpicker.image = image
           cropViewController.dismiss(animated: true, completion: nil)
       }

       func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
           let image = info[.originalImage] as! UIImage
           guard let pickerImage = (info[UIImagePickerController.InfoKey.originalImage] as? UIImage) else { return }
           
           let cropController = CropViewController(croppingStyle: .default, image: pickerImage)
           cropController.delegate = self
           cropController.customAspectRatio = CGSize(width: 100, height: 100)
           
           //今回は使わないボタン等を非表示にする。
           cropController.aspectRatioPickerButtonHidden = true
           cropController.resetAspectRatioEnabled = true
           cropController.rotateButtonsHidden = true
           
           //cropBoxのサイズを固定する。
           cropController.cropView.cropBoxResizeEnabled = true
           //pickerを閉じたら、cropControllerを表示する。
           picker.dismiss(animated: true) {
               self.present(cropController, animated: true, completion: nil)
           }
       }
        


}

