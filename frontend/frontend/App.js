import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './Home/Login';
import SignUpScreen from './Home/Signup'; 
//import ForgotPasswordScreen from './ForgotPasswordScreen'; // Assume this is another component you created

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="SignUp" component={SignUpScreen} />
        
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
