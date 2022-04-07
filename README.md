# Iris_Segmentation_with_U-Net_and_V_Net

_Ayan Banerjee, Chinmoy Ghosh, Satyendra Nath Mandal_

Iris segmentation contains the most significant character in the iris recognition system. An accurate iris segmentation helps to increase the accuracy of iris recognition in any biometric system. However, the robustness and efficiency of conventional iris segmentation methodologies facing massive challenged in a non-cooperative environment because of unfavorable factors, for instance, blur, occlusion, off-axis, low resolution, motion, and specular reflections. These factors severely affects the accuracy of the iris segmentation approaches. In this article, a novel Iris segmentation approaches has been obtained with V-Net architectures to accurately localize the boundaries of the iris image with semantic segmentation mask synthesis. A novel image processing technique: YCrCb and HSV color space has also been utilized to select saliency point set and to recover the boundary of the iris. Not only that, a detailed analytical study has been obtained with the U-Net architecture to understand what the drawbacks of the U-Net architectures are and how V-Net can overcome it. Experimental Results consolidate the fact that the iris segmentation with V-Net achieve 95.6\% mean IOU value whereas, U-Net can only achieve 92.3\%. So V-Net can easily outperforms the existing state-of-the-art-approaches on the challenging UBIRIS database.

**Paper LinK:** https://link.springer.com/article/10.1007/s42979-022-01113-0

I would like to thanks @arijit-hub to helping me out for the pytorch implementation and debugging the codes.

