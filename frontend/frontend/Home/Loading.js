import React, { useEffect } from 'react';
import { View, Text, StyleSheet, ActivityIndicator, Alert } from 'react-native';
import { getFirestore, collection, getDocs, query, where } from 'firebase/firestore';
import { db,auth } from '../database/database';

const LoadingScreen = ({ navigation, route }) => {
  const { companyName, description } = route.params;

  useEffect(() => {
    const fetchSlogan = async () => {
      try {
        // Make sure user is authenticated
        
        
        const user = auth.currentUser;
        if (!user) {
          Alert.alert("No User", "No user is currently signed in.");
          navigation.navigate('Login');
          return;
        }

        const response = await fetch('http://192.168.1.27:5000/generate-slogan', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ companyName, description }),
        });
        
        const json = await response.json();
        console.log(db, auth);  // Check if these are undefined

        if (response.ok) {
          // Save to Firestore with user's email
          await db.collection('slogans').doc(user.email).set({
            companyName,
            description,
            slogan: json.slogan,
            userEmail: user.email,  // Storing user's email with the slogan
            
          });
          
          navigation.navigate('Output', { companyName, description, slogan: json.slogan });
        } else {
          console.log('Response Status:', response.status);
          throw new Error(json.error || 'Failed to generate slogan');
        }
      } catch (error) {
        console.error('Fetch Error:', error);
        Alert.alert('Error', 'Failed to generate slogan: ' + error.message);
      }
    };

    fetchSlogan();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Generating your slogan...</Text>
      <ActivityIndicator size="large" color="#0000ff" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    marginBottom: 20,
  },
});

export default LoadingScreen;
