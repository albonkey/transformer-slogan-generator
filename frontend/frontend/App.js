import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { View } from "react-native";
import Icon from "react-native-vector-icons/MaterialIcons";
// Import your screens
import LoginScreen from './Home/Login';
import SignUpScreen from './Home/Signup';
import HomeScreen from './Home/Home';
import SloganDisplayScreen from './Home/Output';
import LoadingScreen from './Home/Loading';
import ProfileScreen from './Home/ProfileScreen';
import HistoryScreen from './Home/HistoryScreen';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

// Define a function to create home stack navigator that includes login and signup
function AuthStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Login" component={LoginScreen} options={{ headerShown: false }} />
      <Stack.Screen name="SignUp" component={SignUpScreen} options={{ headerShown: false }} />
      <Stack.Screen name="Home" component={HomeScreen} options={{ headerShown: false }} />
      <Stack.Screen name="Loading" component={LoadingScreen} options={{ headerShown: false }} />
      <Stack.Screen name="Output" component={SloganDisplayScreen} options={{ headerShown: false }} />
      <Stack.Screen name="History" component={HistoryScreen} options={{ headerShown: false }} />

    </Stack.Navigator>
  );
}

// Tab Navigator only for Home and History
function HomeTabNavigator() {
  return (
    <Tab.Navigator screenOptions={{ tabBarShowLabel: false }}>
      <Tab.Screen name="Home" component={HomeScreen} options={{
          tabBarIcon: (color) => (
            <View
              style={{
                height: 40,
                width: 60,
                justifyContent: "center",
                alignItems: "center",
                backgroundColor: "white",
                borderColor: "orange",
                borderWidth: 2,
                borderRadius: 30, 
              }}
            >
              <Icon name="home" color={color} size={28} />
            </View>
          ),
          headerShown: false,
        }} />
      <Tab.Screen name="History" component={HistoryScreen}options={{
          tabBarIcon: (color) => (
            <View
              style={{
                height: 40,
                width: 60,
                justifyContent: "center",
                alignItems: "center",
                backgroundColor: "white",
                borderColor: "orange",
                borderWidth: 2,
                borderRadius: 30, 
              }}
            >
              <Icon name="lock-clock" color={color} size={28} />
            </View>
          ),
          
        }} />
    </Tab.Navigator>
  );
}

// Main component with Navigation
const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Auth" component={AuthStack} />
        <Stack.Screen name="Main" component={HomeTabNavigator} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
