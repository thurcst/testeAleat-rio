def house_model(y_new):

    xs =  np.array( [ -1,0,1,2,3,4 ] , dtype = float)
    ys =  np.array( [ -1,0,1,2,3,4 ] , dtype = float)
    model = tf.keras.Sequential( [keras.layers.Dense( units = 1, input_shape = [1] )])
    model.compile(optimizer = "sgd" ,  loss = ' mean_squared_error')
    model.fit(xs,ys, epochs = 500)
    
    print("ia eh brabor")
    print("Eu tenho que ter vergonha na cara e aprender Py kkkk")
    
    return model.predict (y_new)[0]
