import React, { useEffect, useState } from 'react';
import { View, FlatList, StyleSheet } from 'react-native';

import { db, auth } from '../database/database';
import SloganItem from './SloganItem';  // Ensure the correct path to SloganItem component

const HistoryScreen = () => {
  const [slogans, setSlogans] = useState([]);

  useEffect(() => {
    const fetchSlogans = async () => {
      const user = auth.currentUser;
      if (!user) {
        console.log("No user is currently signed in.");
        return;
      }

      const doc = await db.collection('slogans').doc(user.email).get();
      if (doc.exists) {
        setSlogans([doc.data()]);  // Assuming multiple slogans per user stored in one document
      } else {
        console.log("No such document!");
      }
    };

    fetchSlogans();
  }, []);

  return (
    <View style={styles.container}>
      <FlatList
        data={slogans}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => <SloganItem item={item} />}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#fff',
  }
});

export default HistoryScreen;
